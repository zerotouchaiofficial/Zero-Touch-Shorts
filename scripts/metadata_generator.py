# ================================================================
# 🏷️ Auto Title + Description + Hashtag Generator
# ================================================================
import random, re

TITLE_TEMPLATES = [
    "🤯 {keyword} Facts That Will BLOW Your Mind!",
    "Did You Know? 🧠 {keyword} Facts #shorts",
    "SHOCKING Facts Nobody Tells You! 🔥 #{n}",
    "You Won't Believe These {keyword} Facts! 😱",
    "🧠 Mind-Blowing Facts Vol.{n} | #shorts",
    "Facts That Sound Fake But Are 100% TRUE! 🤯",
    "Things You Never Knew About {keyword}! 🔥",
    "WOW! These Facts Are UNREAL 😲 #shorts",
    "🔥 Crazy Facts That Will Change How You Think!",
    "Stop Scrolling — These Facts Are WILD 🤯",
    "FACTS: Vol.{n} — Guaranteed to Surprise You! ✨",
    "Did You Know THIS? 😱 {keyword} Edition",
    "🌍 Amazing Facts You Didn't Learn in School!",
    "These Facts Hit Different 🤯 #didyouknow",
    "🧠 Random Facts That Are Actually Incredible!",
    "Mind-Blowing Facts Nobody Talks About 🤯 #{n}",
    "🔥 {keyword} Facts That Sound Fake But Are Real!",
    "😱 Facts That Will Keep You Up At Night! #{n}",
    "You NEED To Know These {keyword} Facts! 🧠",
    "🌟 Incredible Facts To Blow Your Mind Vol.{n}",
]

STOP_WORDS = {
    'the','a','an','is','are','was','were','be','been','have','has',
    'had','do','does','did','will','would','could','should','may',
    'might','shall','can','to','of','in','on','at','by','for','with',
    'about','as','into','through','during','before','after','above',
    'below','from','up','down','and','but','or','nor','so','yet',
    'both','either','not','only','own','same','than','too','very',
    'just','that','this','these','those','it','its','they','them',
    'their','there','when','where','which','who','how','what','if','then',
}

def extract_keyword(facts):
    freq = {}
    for fact in facts:
        for w in re.findall(r'\b[a-zA-Z]{5,}\b', fact.lower()):
            if w not in STOP_WORDS:
                freq[w] = freq.get(w, 0) + 1
    if not freq:
        return 'Amazing'
    top = sorted(freq.items(), key=lambda x: x[1], reverse=True)
    return top[0][0].capitalize()

def generate_title(facts, video_number):
    keyword  = extract_keyword(facts)
    n        = video_number
    template = TITLE_TEMPLATES[video_number % len(TITLE_TEMPLATES)]
    return template.format(keyword=keyword, n=n)[:98]

def generate_description(facts, video_number):
    lines = [
        "🧠 Welcome to Did You Know? — your daily dose of mind-blowing facts!",
        "",
        f"📋 In this Short (Video #{video_number}):",
    ]
    for i, f in enumerate(facts[:5], 1):
        lines.append(f'  #{i} — {f[:80]}{"..." if len(f)>80 else ""}')
    if len(facts) > 5:
        lines.append(f'  ... and {len(facts)-5} more incredible facts!')
    lines += [
        "",
        "─" * 40,
        "📌 SUBSCRIBE for daily facts that will blow your mind!",
        "🔔 Hit the bell so you never miss a new Short!",
        "❤️  Like if you learned something new today!",
        "💬 Comment your favourite fact below!",
        "📤 Share with someone who loves facts!",
        "─" * 40,
        "",
        "📚 Sources: Curated from public knowledge databases",
        "🎵 Music: Original composition",
        "",
        "─" * 40,
        "🏷️ HASHTAGS",
        "",
        generate_hashtags(facts, inline=True),
    ]
    return "\n".join(lines)[:4900]

CORE_TAGS = [
    '#shorts','#didyouknow','#facts','#mindblowingfacts','#funfacts',
    '#amazingfacts','#learnsomething','#knowledge','#factsyoudidntknow',
    '#factsoflife','#education','#shortsvideo','#youtubeshorts',
    '#viral','#trending','#science','#randomfacts','#dailyfacts',
    '#mindblown','#unbelievable','#incredible','#wow','#psychology',
    '#interestingfacts','#history','#factcheck','#learneveryday',
]

def generate_hashtags(facts, inline=False):
    keyword  = extract_keyword(facts)
    dynamic  = [f'#{keyword.lower()}facts', f'#{keyword.lower()}']
    all_tags = list(dict.fromkeys(dynamic + CORE_TAGS))[:30]
    return ' '.join(all_tags) if inline else all_tags

def generate_metadata(facts, video_number):
    return {
        'title':       generate_title(facts, video_number),
        'description': generate_description(facts, video_number),
        'tags':        generate_hashtags(facts),
        'category':    '27',
        'privacy':     'public',
    }
