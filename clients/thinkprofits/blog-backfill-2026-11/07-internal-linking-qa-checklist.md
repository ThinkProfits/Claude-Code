**Title tag:** Internal Linking Checklist: Pre-Publish QA | ThinkProfits (57 characters)

**Meta description:** Use this internal linking checklist before a post goes live: orphan checks, anchor text, links to service pages and redirect clean-up, in about 15 minutes. (155 characters)

**Slug:** `/digital-news/internal-linking-qa-checklist/`

**Primary keyword:** internal linking checklist

**Secondary keywords:** internal linking, internal links SEO, orphan pages, anchor text SEO, broken internal links, internal link audit, internal linking best practices, SEO checklist

**Search intent:** Informational with a practical, do-it-now angle. The reader is a marketer, owner or writer who is about to publish a post and wants a short QA routine, not a full site audit.

**Category:** SEO

---

# Internal Linking Checklist: QA Before a Post Goes Live

[IMAGE: ThinkProfits branded hero placeholder | alt: Internal linking checklist for reviewing a blog post before it goes live | file: /images/blog/wp/tp-branded-placeholder.jpg]

> **Quick answer:** An internal linking checklist is a short QA pass you run before publishing. Confirm that existing pages link to the new post, that the post links to the service page it supports, that every anchor describes its destination, and that no link is broken or pointing at a redirect. On a typical post it takes us 10 to 15 minutes.

Most internal linking advice is written for site-wide audits. That work has its place, but the cheapest moment to get links right is just before a post goes live, while you still remember why you wrote it and nobody has shared the URL yet. This internal linking checklist is the pre-publish QA we run on blog posts for our own site and for client sites, whether they run on WordPress, Lovable or a headless setup. It covers links pointing into the new page, links out to the pages that bring in enquiries, anchor text, broken and redirecting links, and the difference between navigation links and links in the body copy. It will not guarantee rankings. It does make sure search engines and readers can find the post and leave it for somewhere useful.

## The pre-publish internal linking checklist

The whole routine fits in one table, and each row gets its own section below.

| Check | What a pass looks like | Common failure |
|---|---|---|
| Links in | At least two existing, related pages link to the new post in their body copy | Only the blog index and the sitemap point to it |
| Links out to service pages | The post links to the service page its topic supports | It links only to other blog posts, or to nothing |
| Anchor text | Each anchor describes the destination and makes sense read on its own | "Click here", "this post", or the same exact-match keyword every time |
| Status | Every internal link goes straight to a live page | Links to old URLs that redirect, or to a deleted post |
| Link format | Links are real `<a href>` elements in the rendered HTML | A button or div with a click handler and no URL |
| Placement | Links sit in sentences that explain why the reader would click | Everything piled into a list at the bottom |
| Repeats | No page linked more than twice from the same post | The same service page linked five times |

We keep this table in the publishing doc and tick it off for every post, because a check that lives in someone's head gets skipped on deadline week.

## Orphan check: give the new post links pointing in

A new post needs at least one link from another page on your site, and ideally a few from closely related content. Google's own [link best practices](https://developers.google.com/search/docs/crawling-indexing/links-crawlable) put it plainly: every page you care about should have a link from at least one other page on your site. A post with no internal links pointing at it (an orphan page) depends on the blog index, the XML sitemap and whatever gets shared on social.

The fix takes a few minutes if you do it before publishing:

1. **Find two to four related pages.** Search your own site for the post's main topic and pick older posts or service pages that a reader of those pages would genuinely want to read next. For this post, that meant our pieces on [sitemap hygiene during a rebuild](/digital-news/sitemap-hygiene-website-rebuild/) and [content consolidation](/digital-news/content-consolidation-without-traffic-loss/).
2. **Add a contextual link on each.** Edit a sentence on the older page so the link reads naturally, rather than bolting a "Related reading" line on the end, and note each edit in your publishing log.
3. **Confirm the post appears in its category listing.** This is a backup route in, not a replacement for body links.

Search Console's Links report shows which pages link to a given URL, but Google describes it as a sample of links it has already found, so it helps with older pages rather than a post going live today.

## Link out to the pages that bring in enquiries

Every blog post should link to at least one page where a reader can act on what they just read. For most service businesses that is a service page, and blog posts that only link to other blog posts send readers in circles.

Ask one question of each draft: if this reader decides they want help, which page should they land on? A post about map pack rankings should point to [local SEO](/seo-services/local-seo/). A post about technical clean-up belongs next to an [SEO audit](/seo-audit/). Our guide to [service pages, location pages and blog posts](/digital-news/service-page-location-page-blog-post/) covers how those three page types split the work, and the blog's job is usually to answer the question and hand off.

One link to the right service page, placed where the post mentions that service, beats three links stuffed into the closing paragraph. If a post has no natural service page to link to, either the topic is drifting from what you sell or you are missing a page.

## Anchor text that describes the destination

Anchor text should tell the reader, and Google, what is on the other side of the link. Google's guidance asks for anchor text that is descriptive, reasonably concise and relevant to both pages, and it calls out generic text like "click here" as unhelpful.

A quick test we use: read only the linked words, out of context. "Our [content writing services](/content-writing-services/)" passes. "Learn more here" fails, because "here" could be anything. Three habits keep anchors clean:

- **Describe, don't repeat.** Vary the wording naturally across the site rather than using one exact-match keyword for every link to a page, which reads as forced and edges toward the keyword stuffing that Google's spam policies prohibit.
- **Keep it short.** A few words is usually enough, since linking a whole sentence makes the destination harder to guess.
- **Match the promise.** If the anchor says "pricing", the destination should show pricing. A mismatch costs trust the first time a reader clicks.

Image links follow the same logic. When an image is the link, Google uses its alt text as the anchor, so a blank alt attribute on a linked image is a link with no label.

## Broken, redirecting and non-crawlable links

Every internal link should resolve directly to a live page, with no 404 and no redirect in between. This check fails most often on rebuilt or consolidated sites, where old URLs live on inside older posts.

Redirects do work, so a link to an old URL is not a disaster. Google's documentation notes that its crawlers follow up to 10 redirect hops, but its [site move guidance](https://developers.google.com/search/docs/crawling-indexing/site-move-with-url-changes) still recommends updating internal links to the new URLs and avoiding redirect chains. Linking straight to the final URL is faster for the reader and removes a dependency on a redirect rule someone might delete next year.

How we run this check before publishing:

1. **Click every link in the preview.** Watch the address bar: if the URL changes after the page loads, you linked to a redirect.
2. **Check trailing slashes and case.** On many sites `/seo-audit` and `/seo-audit/` are different URLs, and one redirects to the other. Copy URLs from the live address bar rather than typing them.
3. **Inspect the rendered HTML on JavaScript sites.** On Lovable and other React builds, confirm each link is a standard `<a href>` element in the rendered page. Google says it can't reliably extract URLs from elements without an `href`, so a styled button with only a click handler may be invisible to crawlers.

For site-wide sweeps, a crawler such as Semrush Site Audit flags broken and redirected internal links in bulk. Our [free SEO audit tool](/free-seo-audit-tool/) gives a quick first look at a single page if you want a second opinion before launch.

## Navigation links vs contextual links

Navigation, footer and sidebar links appear on every page. Contextual links sit inside the body copy and carry meaning from the sentences around them, and a healthy post needs them because navigation is identical everywhere.

Google's guidance notes that the words before and after a link matter, and it advises against stacking links right next to each other. In practice that means:

- **Link inside the sentence that explains the destination.** "If your city pages compete with each other, see how we [diagnose city landing page cannibalization](/digital-news/city-landing-page-cannibalization-search-console/)" gives the reader a reason to click.
- **Don't treat the menu as your internal linking.** A service page linked from the header on every page still benefits from a body link in a post that discusses that service, because the body link says why it is relevant.
- **Cap repeats at two.** Linking the same page over and over in one post adds noise, not signal, and readers start ignoring the underlines.

We would rather ship five strong links than pad a post to eight weak ones.

## FAQ

### What is an orphan page?

An orphan page is a page with no internal links pointing to it from elsewhere on your site. Search engines may still find it through your XML sitemap, but readers can't reach it by browsing, and it carries no context from related pages. New blog posts become orphans by default unless you add links to them from older content.

### How many internal links should a blog post have?

Google does not publish a target number. We use five or more distinct, relevant destinations on posts over 1,200 words, including at least one service page, and we never link the same page more than twice in one post. If a post can't reach five useful links, that usually means the site needs more supporting pages, not weaker links.

### Should internal links open in a new tab?

We keep internal links in the same tab, because readers expect to move around one site in one window and can use the back button. External links to sources are different, and we open those in a new tab so readers keep their place.

### Is it bad to link to a URL that redirects?

It won't usually break anything, since Google follows redirects, but Google's own guidance is to update internal links to the final URL and avoid chains. Each extra hop slows the page for the reader, and an internal link that depends on a redirect fails the day someone tidies up the redirect list.

**Want a second set of eyes on your next launch?**

An internal linking check is easy to skip and tedious to fix later. If you want help building it into your publishing routine, or a review of how your blog supports your [SEO services](/seo-services/) pages, we are happy to talk it through. For a quick first look at one page, run our [free SEO audit tool](/free-seo-audit-tool/).

**[Book My Free Consultation](/contact/)**
