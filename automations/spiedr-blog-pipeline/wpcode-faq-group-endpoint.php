<?php
/**
 * SPIEDR: create Easy Accordion FAQ groups over the REST API.
 *
 * WPCode snippet. Type: PHP Snippet. Insert method: Auto Insert, Run Everywhere.
 * DRAFT (2026-10-28), not installed. See README.md in this folder for the install and test plan.
 *
 * Why a route instead of register_post_meta(): Easy Accordion keeps a group's questions in the
 * serialized post meta `sp_eap_upload_options` and its display settings (schema on/off, colours,
 * first-open) in `sp_eap_shortcode_options`. Neither is registered for REST, so the wp-spiedr MCP and
 * Make's WordPress module can't write them. Exposing both keys as raw REST meta would let any caller
 * write the plugin's whole settings array. This route only accepts questions and answers, copies
 * every display setting from an existing group, and always switches schema on.
 *
 * POST /wp-json/spiedr/v1/faq-group
 *   title     string  required  Group title, e.g. "FAQ for <post title>".
 *   faqs      array   optional  [{ "question": "...", "answer": "<p>...</p>" }, ...]
 *   faq_html  string  optional  The FAQ block as HTML: each <h3> is a question, everything until the
 *                               next <h3> is its answer. Use this from Make (module 23's `faq` output).
 *   Send `faqs` or `faq_html`. Returns { id, shortcode, title, count, created }.
 *
 * Re-sending the same title returns the existing group instead of creating a duplicate, so a Make
 * retry is safe. Requires a user who can edit posts (the Make and Easy MCP AI connections both are).
 */

defined( 'ABSPATH' ) || exit;

// Group whose display settings new groups copy (FAQ for Wildfire Protection for Critical Infrastructure).
if ( ! defined( 'SPIEDR_FAQ_TEMPLATE_GROUP' ) ) {
	define( 'SPIEDR_FAQ_TEMPLATE_GROUP', 8925 );
}

add_action( 'rest_api_init', function () {
	register_rest_route( 'spiedr/v1', '/faq-group', array(
		'methods'             => 'POST',
		'permission_callback' => function () {
			return current_user_can( 'edit_posts' );
		},
		'args'                => array(
			'title'    => array(
				'type'              => 'string',
				'required'          => true,
				'sanitize_callback' => 'sanitize_text_field',
			),
			'faqs'     => array(
				'type'  => 'array',
				'items' => array(
					'type'       => 'object',
					'properties' => array(
						'question' => array( 'type' => 'string' ),
						'answer'   => array( 'type' => 'string' ),
					),
				),
			),
			'faq_html' => array( 'type' => 'string' ),
		),
		'callback'            => 'spiedr_rest_create_faq_group',
	) );
} );

/**
 * Splits an FAQ HTML block into question/answer pairs: <h3>Q</h3> followed by its answer.
 */
function spiedr_faqs_from_html( $html ) {
	$faqs = array();
	if ( preg_match_all( '#<h3[^>]*>(.*?)</h3>(.*?)(?=<h3|\z)#is', $html, $matches, PREG_SET_ORDER ) ) {
		foreach ( $matches as $m ) {
			$faqs[] = array(
				'question' => $m[1],
				'answer'   => $m[2],
			);
		}
	}
	return $faqs;
}

function spiedr_rest_create_faq_group( WP_REST_Request $request ) {
	if ( 'sp_easy_accordion' !== get_post_type( SPIEDR_FAQ_TEMPLATE_GROUP ) ) {
		return new WP_Error( 'spiedr_faq_no_template', 'Template FAQ group ' . SPIEDR_FAQ_TEMPLATE_GROUP . ' is missing.', array( 'status' => 500 ) );
	}

	$title = $request->get_param( 'title' );
	$faqs  = $request->get_param( 'faqs' );
	if ( empty( $faqs ) && $request->get_param( 'faq_html' ) ) {
		$faqs = spiedr_faqs_from_html( $request->get_param( 'faq_html' ) );
	}

	$items = array();
	foreach ( (array) $faqs as $faq ) {
		$question = trim( wp_strip_all_tags( html_entity_decode( $faq['question'] ?? '', ENT_QUOTES, 'UTF-8' ) ) );
		$answer   = trim( wp_kses_post( $faq['answer'] ?? '' ) );
		if ( '' === $question || '' === wp_strip_all_tags( $answer ) ) {
			continue;
		}
		$items[] = array(
			'accordion_content_title'       => $question,
			'accordion_content_description' => $answer,
		);
	}
	if ( ! $items ) {
		return new WP_Error( 'spiedr_faq_empty', 'No complete question/answer pairs found.', array( 'status' => 400 ) );
	}

	// Same title already exists: hand back that group instead of making a second one.
	$existing = get_posts( array(
		'post_type'      => 'sp_easy_accordion',
		'post_status'    => array( 'publish', 'draft', 'private' ),
		'title'          => $title,
		'posts_per_page' => 1,
		'fields'         => 'ids',
	) );
	if ( $existing ) {
		return spiedr_faq_group_response( $existing[0], $title, count( $items ), false );
	}

	$group_id = wp_insert_post( array(
		'post_type'   => 'sp_easy_accordion',
		'post_status' => 'publish',
		'post_title'  => $title,
	), true );
	if ( is_wp_error( $group_id ) ) {
		return $group_id;
	}

	update_post_meta( $group_id, 'sp_eap_upload_options', array(
		'eap_accordion_type'       => 'content-accordion',
		'accordion_content_source' => $items,
		'eap_post_type'            => 'sp_accordion_faqs',
		'post_order_by'            => 'date',
		'post_order'               => 'DESC',
	) );

	$display                          = (array) get_post_meta( SPIEDR_FAQ_TEMPLATE_GROUP, 'sp_eap_shortcode_options', true );
	$display['eap_schema_markup']     = true;
	$display['eap_accordion_uniq_id'] = 'sp_easy_accordion-' . $group_id;
	update_post_meta( $group_id, 'sp_eap_shortcode_options', $display );

	return spiedr_faq_group_response( $group_id, $title, count( $items ), true );
}

function spiedr_faq_group_response( $group_id, $title, $count, $created ) {
	return rest_ensure_response( array(
		'id'        => (int) $group_id,
		'shortcode' => '[sp_easyaccordion id="' . (int) $group_id . '"]',
		'title'     => $title,
		'count'     => $count,
		'created'   => $created,
	) );
}
