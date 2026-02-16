# ================================================================
# 🏷️ SEO-Optimised Metadata — High CTR Titles + Auto Pin Comment
# ================================================================
import random, re

# ── High-CTR title templates (curiosity gap + numbers) ────────────
TITLE_TEMPLATES = [
    "🤯 Wait Until You Hear Fact #{last}... #{n}",
    "Did You Know? 🧠 These {n} Facts Sound Fake But Are TRUE!",
    "SHOCKING: {keyword} Facts Nobody Talks About 🔥",
    "You Won't Believe Fact #{last} 😱 #{n} Mind-Blowing Facts",
    "🧠 {n} Facts That Will Ruin How You See The World",
    "Stop Everything — Fact #{last} Changed My Life 🤯",
    "🔥 {n} {keyword} Facts That Went VIRAL For a Reason",
    "The Fact At #{last} Has No Right Being This Wild 😲",
    "🌍 {n} Facts Even Smart People Get Wrong!",
    "POV: You Just Learned {n} Things Nobody Taught You 🧠",
    "😱 Fact #{last} Broke The Internet — Did You Know This?",
    "🔥 These {n} Facts Are Illegal To Not Know",
    "🤯 {keyword} Facts That Sound Like Lies (But Aren't!)",
    "Nobody Is Talking About These {n} Facts 👀",
    "⚡ {n} Facts Dropped In {dur} Seconds — Can You Keep Up?",
    "🧠 Your Brain Will Hurt After These {n} {keyword} Facts",
    "Fact #{last} Is The Reason I Can't Sleep At Night 😳",
    "🌟 {n} Random Facts That Are Actually Mind-Blowing Vol.{vol}",
    "⚡ These {n} Facts Hit Different At 3AM 🤯",
    "😱 {keyword} Facts Your Teachers Were Too Scared To Share",
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
    n        = len(facts)
    last     = n                           # "Wait for fact #7" hook
    vol      = (video_number // 10) + 1
    # Calculate approx duration for title
    dur      = f'{n*6}s'
    template = TITLE_TEMPLATES[video_number % len(TITLE_TEMPLATES)]
    title    = template.format(
        keyword=keyword, n=n, last=last, vol=vol, dur=dur)
    return title[:98]

# ── Description — first line is a question (shows in search) ──────
def generate_description(facts, video_number):
    keyword = extract_keyword(facts)
    n       = len(facts)
    lines   = [
        # Hook question — appears in YouTube search results
        f"Did you know that {facts[0][:80]}...? 🤯",
        "",
        f"Here are {n} mind-blowing facts that will change how you "
        f"see the world forever!",
        "",
        "─" * 40,
        f"📋 Facts in this video:",
    ]
    for i, f in enumerate(facts, 1):
        lines.append(
            f'  {i}. {f[:75]}{"..." if len(f)>75 else ""}')
    lines += [
        "",
        "─" * 40,
        "👇 COMMENT which fact shocked you most!",
        "👍 LIKE if you learned something new!",
        "🔔 SUBSCRIBE + Bell for daily mind-blowing facts!",
        "📤 SHARE with someone who loves facts!",
        "",
        "─" * 40,
        "📚 Sources: Curated from public knowledge databases",
        "🎵 Music: Original ambient composition",
        "",
        "📌 Watch more: youtube.com/@DidYouKnowFacts",
        "",
        "─" * 40,
        "",
        generate_hashtags(facts, inline=True),
    ]
    return "\n".join(lines)[:4900]

# ── Rotating tag sets — avoids looking spammy to algorithm ────────
TAG_SETS = [
    # Set A — Science focus
    ['#shorts','#didyouknow','#facts','#science','#mindblowingfacts',
     '#funfacts','#amazingfacts','#education','#youtubeshorts',
     '#viral','#trending','#psychology','#randomfacts','#wow',
     '#mindblown','#unbelievable','#incredible','#learneveryday',
     '#factsyoudidntknow','#knowledgeispath'],
    # Set B — General viral
    ['#shorts','#didyouknow','#facts','#viral','#foryou',
     '#fyp','#trending','#mindblowindfacts','#funfacts',
     '#amazingfacts','#youtubeshorts','#education','#wow',
     '#omg','#factsoflife','#dailyfacts','#shortsvideo',
     '#interestingfacts','#unbelievable','#incredible'],
    # Set C — Learning focus
    ['#shorts','#learnontiktok','#learnsomething','#didyouknow',
     '#facts','#education','#knowledge','#science','#history',
     '#psychology','#mindblowindfacts','#amazingfacts',
     '#youtubeshorts','#trending','#viral','#factcheck',
     '#randomfacts','#wow','#incredible','#mindblown'],
    # Set D — Curiosity focus
    ['#shorts','#didyouknow','#curiosity','#facts','#mindblowindfacts',
     '#funfacts','#amazingfacts','#education','#youtubeshorts',
     '#viral','#wow','#omg','#shocking','#unbelievable',
     '#incredible','#factcheck','#randomfacts','#dailyfacts',
     '#learneveryday','#factsyoudidntknow'],
]

def generate_hashtags(facts, inline=False, video_number=0):
    keyword    = extract_keyword(facts)
    dynamic    = [f'#{keyword.lower()}facts', f'#{keyword.lower()}']
    tag_set    = TAG_SETS[video_number % len(TAG_SETS)]
    all_tags   = list(dict.fromkeys(dynamic + tag_set))[:30]
    return ' '.join(all_tags) if inline else all_tags

# ── Auto pin comment — drives engagement ──────────────────────────
PIN_COMMENT_TEMPLATES = [
    "🤯 Which fact shocked you the MOST? Comment the number below! 👇",
    "😱 Drop a 🧠 if you already knew ALL of these!",
    "👇 Comment the fact number that broke your brain! 🤯",
    "🔥 Which fact are you sharing with your friends? Tell me! 👇",
    "🤯 Type your favourite fact number below! Mine is #{last} 👇",
    "😲 Did ANY of these facts surprise you? Let me know! 👇",
    "🧠 Save this video — you'll want to share these facts later!",
    "👀 Tag a friend who needs to see Fact #{last}! 👇",
    "🤯 Be honest — how many of these did you already know? 👇",
    "💬 Drop '🤯' if Fact #{last} genuinely surprised you!",
]

def generate_pin_comment(facts, video_number):
    template = PIN_COMMENT_TEMPLATES[video_number % len(PIN_COMMENT_TEMPLATES)]
    return template.format(last=len(facts))

def generate_metadata(facts, video_number):
    return {
        'title':       generate_title(facts, video_number),
        'description': generate_description(facts, video_number),
        'tags':        generate_hashtags(facts,
                                         video_number=video_number),
        'category':    '27',        # Education
        'privacy':     'public',
        'pin_comment': generate_pin_comment(facts, video_number),
    }
