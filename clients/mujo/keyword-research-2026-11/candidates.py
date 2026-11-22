"""Candidate keyword universe for Mujo AI + business titles (HS and HE).
Each entry: keyword -> (audience, title/hub). Built from: product titles, GSC queries, the 2026-03
Institution Keywords sheet patterns, and SERP/PAA findings. Reusable: edit and re-run volume pulls."""
C = {}


def add(aud, grp, *kws):
    for k in kws:
        C.setdefault(k.lower(), (aud, grp))


# ---- Hubs / category level
add('HE', 'AI hub (HE)', 'ai textbooks', 'ai textbook', 'artificial intelligence textbook', 'artificial intelligence textbooks',
    'textbooks on artificial intelligence', 'ai textbooks for college', 'ai textbook for college students', 'college ai textbook',
    'ai textbooks for higher education', 'ai curriculum for higher education', 'ai curriculum for colleges',
    'ai courses for college students', 'ai course materials', 'ai courseware', 'ai curriculum', 'artificial intelligence curriculum',
    'ai literacy curriculum', 'ai literacy course', 'ai literacy textbook', 'ai literacy for college students',
    'generative ai textbooks', 'generative ai textbook', 'ai undergraduate textbook', 'introduction to artificial intelligence textbook',
    'ai for non computer science majors', 'ai textbook for business students')
add('HE', 'Applied AI for Business program', 'applied ai for business', 'applied ai for business curriculum', 'applied ai certificate',
    'applied ai diploma', 'ai for business course', 'ai for business curriculum', 'ai business curriculum', 'ai for business syllabus',
    'ai in business course', 'artificial intelligence for business course', 'ai business certificate', 'ai for business textbook',
    'ai for business book', 'artificial intelligence for business textbook')
add('HE', 'Business hub (HE)', 'business textbooks', 'business textbooks for college', 'college business textbooks',
    'business textbook publisher', 'business curriculum for college', 'ai business textbooks')
add('HS', 'AI hub (HS)', 'ai curriculum for high school', 'ai curriculum high school', 'high school ai curriculum',
    'ai textbooks for high school', 'ai textbook for high school', 'artificial intelligence high school curriculum',
    'teaching ai in high school', 'ai class for high school', 'ai course for high school students', 'ai lesson plans for high school',
    'ai lesson plans', 'artificial intelligence lesson plans', 'ai books for high school students', 'ai school textbook',
    'high school ai course', 'cte ai curriculum', 'ai cte pathway', 'ai literacy for high school students',
    'ai literacy curriculum high school')
add('HS', 'Business hub (HS)', 'high school business curriculum', 'high school business textbook', 'business textbook high school',
    'high school business class curriculum', 'business class curriculum', 'cte business curriculum', 'business education curriculum',
    'high school business lesson plans', 'business lesson plans high school', 'introduction to business high school curriculum',
    'intro to business curriculum')
# ---- HS titles
add('HS', 'Foundations of Artificial Intelligence', 'foundations of artificial intelligence', 'foundations of artificial intelligence textbook',
    'foundations of ai', 'intro to ai high school', 'introduction to artificial intelligence high school',
    'artificial intelligence textbook high school')
add('HS', 'AI for Business (HS)', 'ai for business high school', 'ai for business high school curriculum', 'ai in business high school')
add('HS', 'AI Marketing Fundamentals (HS)', 'ai marketing high school', 'ai marketing curriculum', 'ai in marketing high school')
add('HS', 'Entrepreneurship Fundamentals', 'entrepreneurship curriculum', 'entrepreneurship curriculum high school',
    'high school entrepreneurship curriculum', 'entrepreneurship textbook high school', 'entrepreneurship textbook',
    'entrepreneurship books for high school', 'entrepreneurship lesson plans', 'entrepreneurship lesson plans high school',
    'entrepreneurship course high school', 'entrepreneurship fundamentals', 'entrepreneurship fundamentals textbook',
    'teaching entrepreneurship high school', 'entrepreneurship class curriculum', 'entrepreneurship 1 curriculum',
    'texas entrepreneurship curriculum')
add('HS', 'Principles of Business', 'principles of business', 'principles of business textbook', 'principles of business high school',
    'principles of business curriculum', 'principles of business class', 'principles of business marketing and finance',
    'business principles textbook', 'principles of business textbook high school')
# ---- HE titles
add('HE', 'AI Literacy', 'ai literacy', 'artificial intelligence literacy', 'ai literacy book', 'ai literacy textbook for college',
    'artificial intelligence literacy textbook', 'ai literacy course for college')
add('HE', 'AI Literacy for Healthcare', 'ai in healthcare textbook', 'ai literacy for healthcare', 'ai in healthcare course',
    'ai for healthcare professionals course', 'ai in healthcare curriculum', 'ai in healthcare education', 'healthcare ai textbook',
    'ai for nursing students', 'ai in nursing education')
add('HE', 'AI Business Analytics', 'business analytics textbook', 'business analytics textbooks', 'ai business analytics',
    'business analytics fundamentals', 'fundamentals of business analytics', 'business analytics course',
    'business analytics curriculum', 'ai in business analytics', 'business analytics with ai')
add('HE', 'AI Accounting Principles', 'ai accounting textbook', 'ai in accounting textbook', 'ai in accounting book',
    'accounting principles textbook', 'ai in accounting course', 'artificial intelligence in accounting', 'ai accounting course',
    'accounting textbook with ai', 'ai in accounting curriculum', 'intro to accounting textbook')
add('HE', 'AI Sales Fundamentals', 'ai sales textbook', 'ai in sales course', 'sales textbook', 'sales fundamentals textbook',
    'ai for sales training', 'ai in sales book', 'professional selling textbook')
add('HE', 'AI Project Management', 'ai project management book', 'ai in project management book', 'ai project management course',
    'project management textbook', 'ai in project management', 'project management textbook with ai', 'ai project management textbook')
add('HE', 'AI for HR Management', 'ai hr textbook', 'ai in human resource management', 'ai in human resources book',
    'human resource management textbook', 'ai in hr course', 'hr management textbook', 'ai for hr course',
    'artificial intelligence human resource management')
add('HE', 'AI for Entrepreneurs', 'ai for entrepreneurs', 'ai for entrepreneurship', 'artificial intelligence for entrepreneurs',
    'ai entrepreneurship course', 'ai for entrepreneurs book', 'entrepreneurship textbook college', 'ai entrepreneurship textbook')
add('HE', 'AI Business Administration', 'ai business administration', 'ai in business administration', 'business administration textbook',
    'intro to business textbook', 'introduction to business textbook', 'ai business administration course', 'business administration ai')
add('HE', 'AI Business Writing', 'ai business writing', 'ai for business writing', 'business writing textbook',
    'business communication textbook', 'business communication textbook with ai', 'ai business communication',
    'business writing course', 'ai writing for business')
add('HE', 'Generative AI for Business', 'generative ai for business', 'generative ai for business book',
    'generative ai for business textbook', 'generative ai for business course', 'generative ai course', 'generative ai in business',
    'generative ai for business leaders')
add('HE', 'Prompt Engineering and LLMs', 'prompt engineering textbook', 'prompt engineering course', 'prompt engineering curriculum',
    'prompt engineering book', 'llm textbook', 'large language models textbook', 'prompt engineering course for students',
    'large language model course')
add('HE', 'AI Marketing (HE)', 'ai marketing textbook', 'ai marketing book', 'ai in marketing book', 'artificial intelligence marketing textbook',
    'ai in marketing textbook', 'ai marketing course', 'artificial intelligence marketing', 'ai in digital marketing book', 'marketing ai book')

if __name__ == '__main__':
    import json
    print(len(C))
    json.dump(list(C), open('candidates.json', 'w'))
    print(json.dumps(list(C)))
