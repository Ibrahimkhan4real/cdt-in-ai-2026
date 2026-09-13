#!/usr/bin/env python3
"""Generates the static HTML pages from one shared header/footer template.
Implements the Claude Design file "CDT in AI Conference 2026.dc.html" as a multi-page site.
Edit content here, run `python3 build.py`, commit the HTML. No dependencies beyond Python 3."""
from pathlib import Path
import hashlib

def _v(path):
    return hashlib.md5(Path(path).read_bytes()).hexdigest()[:8]
CSS_V = _v("assets/css/site.css")
JS_V = _v("assets/js/site.js")

SITE = "CDT in AI Annual Conference 2026"
EASYCHAIR = "https://easychair.org/conferences/?conf=cdtinaiannualconfere0"
CFP_URL = "https://easychair.org/cfp/coventryuniversitycdtinai2026"
REGISTER = "https://forms.cloud.microsoft/Pages/ResponsePage.aspx?id=mqsYS2U3vkqsfA4NOYr9Txeve1SJEVJCqEbhUMPBqIZUQTRKRkpRMDQ3NTI3MjNDT1paQ0gyVUE4WC4u"
RMAP = "RMAP.Science@coventry.ac.uk"
FONTS = "https://fonts.googleapis.com/css2?family=Source+Sans+3:wght@400;500;600;700&family=Source+Serif+4:opsz,wght@8..60,400;8..60,600&display=swap"

NAV = [
    ("index.html", "Home"), ("call-for-papers.html", "Call for Papers"), ("programme.html", "Programme"),
    ("speakers.html", "Keynotes"), ("reviewers.html", "Reviewers"), ("committee.html", "Committee"),
    ("venue.html", "Venue"), ("contact.html", "Contact"),
]
CAL_BTN = '<button type="button" class="btn btn-outline" data-add-to-calendar>↓ Add the day to your calendar</button>'

def header(active):
    items = "".join(
        f'<li><a href="{href}"{" aria-current=\"page\"" if href == active else ""}>{label}</a></li>'
        for href, label in NAV)
    return f'''<a class="skip-link" href="#main">Skip to content</a>
<div class="top-strip"><div class="wrap"><span>Wednesday 7 October 2026 · 09:00 – 16:30 · EC1 29, Sir Frank Whittle Building</span></div></div>
<header class="site-header">
  <div class="wrap header-row">
    <a class="brand" href="index.html">
      <img src="assets/img/mark.png" width="54" height="54" alt="Coventry University Centre for Doctoral Training in AI">
      <span><span class="title">CDT in AI Annual Conference 2026</span><span class="sub">Artificial Intelligence across Domains</span></span>
    </a>
    <div class="header-actions">
      <p class="deadline-note">Abstracts close 18 September<br><span data-deadline-countdown>Friday 18 September 2026</span></p>
      <div class="header-cta">
        <a class="btn btn-gold" href="{EASYCHAIR}">Submit an abstract</a>
        <a class="btn btn-ghost" href="{REGISTER}">Register to attend</a>
      </div>
      <button class="nav-toggle" aria-expanded="false" aria-controls="site-nav">Menu</button>
    </div>
  </div>
  <nav class="site-nav" id="site-nav" aria-label="Main navigation"><div class="wrap"><ul>{items}</ul></div></nav>
</header>'''

FOOTER = f'''<footer class="site-footer">
  <div class="cols">
    <div>
      <img src="assets/img/mark.png" alt="">
      <p class="ft-title">CDT in AI Annual Conference 2026</p>
      <p class="body">Artificial Intelligence across Domains: Research, Innovation and Impact.<br>Wednesday 7 October 2026 · 09:00 – 16:30<br>EC1 29, Sir Frank Whittle Building<br>Coventry University, Coventry CV1 5DL</p>
    </div>
    <div>
      <p class="ft-label">Take part</p>
      <ul>
        <li><a href="{EASYCHAIR}">Submit an abstract on EasyChair</a></li>
        <li><a href="{REGISTER}">Register to attend</a></li>
        <li><a href="reviewers.html">Become a reviewer</a></li>
        <li><button type="button" class="btn-link" data-add-to-calendar>Add the day to your calendar</button></li>
      </ul>
    </div>
    <div>
      <p class="ft-label">Contact</p>
      <ul>
        <li><a href="mailto:{RMAP}">{RMAP}</a></li>
        <li><a href="committee.html">Organising committee</a></li>
        <li><a href="venue.html">Venue and travel</a></li>
        <li><a href="contact.html">All contacts</a></li>
      </ul>
    </div>
  </div>
  <p class="copyright">© 2026 Centre for Doctoral Training in AI, Coventry University.</p>
</footer>
<script src="assets/js/site.js?v={JS_V}"></script>'''

def page(filename, title, body, description):
    html = f'''<!DOCTYPE html>
<html lang="en-GB">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title} · {SITE}</title>
<meta name="description" content="{description}">
<link rel="icon" href="assets/img/favicon.ico">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="{FONTS}">
<link rel="stylesheet" href="assets/css/site.css?v={CSS_V}">
</head>
<body>
{header(filename)}
<main id="main">
{body}
</main>
{FOOTER}
</body>
</html>
'''
    Path(filename).write_text(html)
    print("wrote", filename)

def page_head(eyebrow, h1, lead, note=""):
    n = f'<p class="note">{note}</p>' if note else ""
    return f'''<header class="wrap page-head"><p class="eyebrow">{eyebrow}</p><h1>{h1}</h1><p class="lead">{lead}</p>{n}</header>'''

TOPICS = [
    ("AI Research, Innovation, Methods, Models and Applications", "New algorithms, architectures, learning methods, evaluation and applied systems."),
    ("AI across Disciplines and Professional Contexts", "AI in engineering, health, business, the arts, education, law and other professional domains."),
    ("Responsible AI: Ethics, Governance, Transparency, Bias and Trust", "Fairness, accountability, explainability, regulation and public trust."),
    ("Generative AI: Knowledge, Human Experience and Societal Impact", "Large language and multimodal models, creativity, knowledge work and society."),
]

FORMATS_HOME = [
    ("20", "MIN", "Paper presentations", "Full-length talks in the midday and afternoon panels, each followed by Q&amp;A. Suited to mature work with results."),
    ("5", "MIN", "Lightning talks", "Short, focused talks in two blocks, well suited to work in its early stages or a single key idea."),
    ("All", "DAY", "Poster presentations", "On display from lunch through the closing session, with authors alongside. Awards presented at 15:45."),
]
FORMATS_CFP = [
    ("20", "MIN", "Paper presentation", "Panel 1 at 11:15 and Panel 2 at 14:00, each followed by Q&amp;A. Suited to mature work with results."),
    ("5", "MIN", "Lightning talk", "Two blocks, at 12:30 and 15:15, with Q&amp;A. Well suited to early-stage work or a single key idea."),
    ("All", "DAY", "Poster presentation", "On display from 13:00 through the closing session, with authors alongside. Awards at 15:45. All first-year students present a poster."),
]
def cells(items):
    return '<div class="cells">' + "".join(f'<div class="cell"><p class="big">{n}<span>{u}</span></p><h3>{h}</h3><p class="desc">{d}</p></div>' for n, u, h, d in items) + '</div>'

KEYNOTE_BIO_1 = "Professor of Computer Science at Coventry University and lead of the Human-Centred Reinforcement Learning theme at the Research Centre for Computational Science and Mathematical Modelling."
KEYNOTE_BIO_FULL = "Leads the Human-Centred Reinforcement Learning theme at Coventry University's Research Centre for Computational Science and Mathematical Modelling. His research spans machine learning, reinforcement learning and AI for cyber-physical systems, with industry projects involving JLR, Rolls-Royce and Orbit Group."
KEYNOTE_BIO_2 = "Appointed Innovate UK BridgeAI Independent Scientific Advisor at The Alan Turing Institute in 2025."
STATS = [("20+", "PhD graduates"), ("25", "Grants secured"), ("£35M", "Research funding")]
def stats(extra=""):
    return f'<div class="stats{extra}">' + "".join(f'<div><p class="n">{n}</p><p class="l">{l}</p></div>' for n, l in STATS) + '</div>'

# ---------------------------------------------------------------- HOME
topics_home = "".join(f'<li><span class="num">0{i}</span><div><h3>{t}</h3><p class="d">{d}</p></div></li>' for i, (t, d) in enumerate(TOPICS, 1))
home = f'''
<section class="wrap hero">
  <h1>Artificial Intelligence across Domains</h1>
  <p class="subtitle">Research, Innovation and Impact</p>
  <p class="lead">A one-day conference showcasing the research of Coventry University postgraduate researchers whose work engages with artificial intelligence.</p>
  <div class="btn-row">
    <a class="btn btn-navy" href="{EASYCHAIR}">Submit an abstract</a>
    <a class="btn btn-outline" href="programme.html">See the programme</a>
    <button type="button" class="btn btn-outline" data-add-to-calendar>Add to calendar</button>
  </div>
</section>

<section class="facts">
  <dl>
    <div><dt>Date</dt><dd>Wed 7 October 2026</dd></div>
    <div><dt>Time</dt><dd>09:00 – 16:30</dd></div>
    <div><dt>Venue</dt><dd>EC1 29, Sir Frank Whittle</dd></div>
    <div><dt>Countdown</dt><dd data-conference-countdown><span class="cd-digits">7 October 2026</span><span class="cd-label"></span></dd></div>
  </dl>
</section>

<section class="now-bar" id="now-bar" hidden>
  <p class="label">Happening now</p><p class="session"></p><p class="next"></p>
</section>

<section class="wrap section">
  <div class="section-head"><h2>Ways to take part</h2><p class="kicker">Twelve slots · one poster exhibition</p></div>
  {cells(FORMATS_HOME)}
  <p class="after-note">Abstracts are 250 words with a 100-word biography, submitted on EasyChair. <a href="call-for-papers.html">Read the full call for participation →</a></p>
</section>

<section class="band-navy section keynote-band">
  <div class="wrap-inner two-col">
    <div class="text">
      <p class="eyebrow">Keynote · 10:00 – 10:40</p>
      <h2>Prof. James Brusey</h2>
      <p class="bio">{KEYNOTE_BIO_1}</p>
      <p class="bio" style="margin-bottom:0">{KEYNOTE_BIO_2}</p>
      {stats()}
      <p style="margin-top:26px"><a class="arrow-link" href="speakers.html">Both keynote sessions →</a></p>
    </div>
    <div class="emblem"><img src="assets/img/mark.png" alt="CDT in AI phoenix emblem"></div>
  </div>
</section>

<section class="wrap section">
  <div class="section-head tight"><h2>Four topic areas</h2><p class="kicker">Choose one on EasyChair</p></div>
  <ol class="numbered">{topics_home}</ol>
</section>

<section class="band section">
  <div class="wrap-inner two-col">
    <div>
      <p class="eyebrow">Who should attend</p>
      <h2 class="h2-mid">Open to CDT in AI postgraduate researchers</h2>
      <p class="body-2 lg" style="margin-bottom:20px">Open to Coventry University CDT in AI postgraduate researchers across all disciplines, along with supervisors and staff of the CDT. All CDT in AI students are expected to attend and to contribute a talk, poster or paper.</p>
      <a class="btn btn-navy" href="{REGISTER}">Register to attend</a>
    </div>
    <div class="narrow">
      <p class="eyebrow">Help review</p>
      <h2 class="h2-mid">Reviewing runs 19 – 24 September</h2>
      <p class="body-2 lg" style="margin-bottom:20px">Students, supervisors and staff each take a small number of abstracts matched to their expertise. Reviews are completed on EasyChair.</p>
      <a class="btn btn-outline" href="reviewers.html">Review criteria</a>
    </div>
  </div>
</section>
'''
page("index.html", "Home", home, "CDT in AI Annual Conference 2026, Coventry University. Artificial Intelligence across Domains: Research, Innovation and Impact. Wednesday 7 October 2026.")

# ---------------------------------------------------------------- CALL FOR PAPERS
topics_cfp = "".join(f'<li class="compact"><span class="num">0{i}</span><span class="t only">{t}</span></li>' for i, (t, _) in enumerate(TOPICS, 1))
cfp = page_head("Call for Participation", "Call for participation",
                "Paper presentations, lightning talks and posters are invited from Coventry University CDT in AI postgraduate researchers across all disciplines.") + f'''
<section class="wrap section no-bottom">
  <ol class="dates">
    <li data-date="2026-09-18T23:59:00" data-deadline-status><span class="stamp mono-date">18.09.26</span><span class="label">Abstracts close</span><span class="detail">250-word abstract and 100-word biography, via EasyChair</span><span class="status"></span></li>
    <li data-date="2026-09-25T23:59:00"><span class="stamp mono-date">25.09.26</span><span class="label">Notification of outcome</span><span class="detail">Authors informed by email, with format and session</span><span class="status"></span></li>
    <li data-date="2026-10-07T16:30:00"><span class="stamp mono-date">07.10.26</span><span class="label">Conference day</span><span class="detail">09:00 – 16:30, EC1 29, Sir Frank Whittle Building</span><span class="status"></span></li>
  </ol>
</section>

<section class="wrap section two-col">
  <div class="wide">
    <h2 class="h2-rule">How to submit</h2>
    <ol class="steps">
      <li><span class="num">01</span><span>Go to the <a href="{EASYCHAIR}">EasyChair submission page</a> and sign in or create a free account.</span></li>
      <li><span class="num">02</span><span>Enter your <strong>abstract (250 words maximum)</strong> and a <strong>short biography (100 words maximum)</strong>.</span></li>
      <li><span class="num">03</span><span>Select your preferred format: paper presentation, lightning talk or poster.</span></li>
      <li><span class="num">04</span><span>Select one of the four topics.</span></li>
      <li><span class="num">05</span><span>Submit before <strong>Friday 18 September 2026</strong>. You can edit your submission until the deadline.</span></li>
    </ol>
    <div class="btn-row">
      <a class="btn btn-gold" href="{EASYCHAIR}">Submit on EasyChair</a>
      <a class="btn btn-outline" href="{CFP_URL}">EasyChair call for papers</a>
    </div>
    <p class="muted" style="font-size:15px;margin-top:22px">Suggestions for the second keynote speaker are welcome alongside your submission.</p>
  </div>
  <div>
    <h2 class="h2-rule">Review and selection</h2>
    <p class="body-2" style="margin-bottom:14px">Every abstract is reviewed by members of the CDT in AI community against the published <a href="reviewers.html">review criteria</a>: relevance, clarity, rigour, originality and impact. Authors are notified of the outcome, and of their allocated format and session, by <strong>25 September 2026</strong>.</p>
    <p class="body-2" style="margin-bottom:20px">There are twelve presentation slots in total: six 20-minute papers and six 5-minute lightning talks, plus the poster exhibition. Where demand exceeds the slots available, the committee may offer an alternative format.</p>
    <div class="callout"><p class="eyebrow">Note</p><p>Registration to attend is separate from abstract submission. <a href="{REGISTER}">Complete the registration form</a> even if you are not presenting.</p></div>
  </div>
</section>

<section class="band-navy section">
  <div class="wrap-inner">
    <div class="section-head"><h2>Presentation formats</h2><p class="kicker">Pick the one that fits your stage of work</p></div>
    {cells(FORMATS_CFP)}
  </div>
</section>

<section class="wrap section">
  <div class="section-head tight"><h2>Topics</h2><p class="kicker">Select one on EasyChair</p></div>
  <ol class="numbered" style="margin-bottom:clamp(34px,4vw,52px)">{topics_cfp}</ol>
  <div class="poster-row">
    <a href="assets/img/poster.png"><img src="assets/img/poster-web.jpg" width="1080" height="1080" loading="lazy" alt="Call for Participation poster for the CDT in AI Conference 2026"></a>
    <div class="text">
      <p class="eyebrow">Share the call</p>
      <h2>Call for Participation poster</h2>
      <p class="body-2" style="margin-bottom:20px;max-width:46ch">Download and share the poster with colleagues in your research centre. The QR code links straight to the EasyChair submission page.</p>
      <a class="btn btn-outline" href="assets/img/poster.png">Open poster image</a>
    </div>
  </div>
</section>
'''
page("call-for-papers.html", "Call for Papers", cfp, "Call for participation and important dates for the CDT in AI Annual Conference 2026 at Coventry University. Abstracts due 18 September 2026.")

# ---------------------------------------------------------------- PROGRAMME
def slot(title, time, kind, presenters=("Presenter TBC",) * 3):
    items = "".join(f"<li>{p}</li>" for p in presenters)
    return f'<div class="slot"><p class="time">{time}</p><h3>{title}</h3><ol>{items}</ol><p class="kind">{kind}</p></div>'
programme = page_head("Programme", "Running order",
                      "Wednesday 7 October 2026 · 09:00 – 16:30 · EC1 29, Sir Frank Whittle Building. Provisional until presenters are confirmed after 25 September.",
                      "Session chairs keep time · load slides during the preceding break") + f'''
<section class="wrap section">
  <div class="view-toggle" role="group" aria-label="Programme view">
    <button type="button" data-view="timeline" aria-pressed="true">Timeline</button>
    <button type="button" data-view="table" aria-pressed="false">Table</button>
  </div>
  <div id="view-timeline">
    <ol class="timeline" id="timeline"></ol>
  </div>
  <div id="view-table" hidden>
    <div class="table-wrap">
      <table class="schedule"><thead><tr><th>Time</th><th>Session</th><th>Notes</th></tr></thead><tbody id="schedule-body"></tbody></table>
    </div>
  </div>
  <p class="after-note">Posters are on display from 13:00 through the closing session, with awards presented at 15:45.</p>
</section>

<section class="band section">
  <div class="wrap-inner">
    <div class="section-head" style="margin-bottom:clamp(24px,3vw,36px)"><h2>Sessions at a glance</h2><p class="kicker">Twelve presentation slots</p></div>
    <div class="cells narrow">
      {slot("Panel 1", "11:15 – 12:15", "20-min papers + Q&amp;A")}
      {slot("Lightning 1", "12:30 – 13:00", "5-min talks + Q&amp;A")}
      {slot("Panel 2", "14:00 – 15:00", "20-min papers + Q&amp;A")}
      {slot("Lightning 2", "15:15 – 15:45", "5-min talks + Q&amp;A")}
    </div>
    <p style="margin-top:26px">{CAL_BTN}</p>
  </div>
</section>
'''
page("programme.html", "Programme", programme, "Running order for the CDT in AI Annual Conference 2026: keynote, panels, lightning talks, poster exhibition and awards.")

# ---------------------------------------------------------------- SPEAKERS
speakers = page_head("Keynote Speakers", "Keynote speakers", "Two keynote sessions anchor the day. The second speaker will be announced ahead of the full programme.") + f'''
<section class="wrap section">
  <article class="speaker first">
    <div class="portrait-col">
      <div class="portrait" id="portrait-brusey"><img src="assets/img/brusey.jpg" width="190" height="238" alt="Prof. James Brusey"></div>
      <p class="slot-label">Keynote 1 of 2</p><p class="slot-time">10:00 – 10:40</p>
    </div>
    <div class="text">
      <h2>Prof. James Brusey</h2>
      <p class="role">Professor of Computer Science, Coventry University, UK</p>
      <p class="bio">{KEYNOTE_BIO_FULL}</p>
      <p class="bio" style="margin-bottom:24px">{KEYNOTE_BIO_2}</p>
      {stats(" on-paper")}
      <p class="muted" style="font-size:15px;margin-top:18px">Keynote 10:00 – 10:40, followed by Q&amp;A until 11:00.</p>
    </div>
  </article>
  <article class="speaker">
    <div class="portrait-col">
      <div class="portrait" id="portrait-keynote-2">Photograph to follow</div>
      <p class="slot-label">Keynote 2 of 2</p><p class="slot-time tbc">Time to be confirmed</p>
    </div>
    <div class="text">
      <h2 style="margin-bottom:16px">Second keynote speaker</h2>
      <p class="bio">Our second keynote will be confirmed ahead of the full programme's publication, and announced to registered attendees by email.</p>
      <p class="bio" style="margin-bottom:0">Suggestions from CDT in AI supervisors and researchers are welcome. Nominations can be sent alongside your <a href="{EASYCHAIR}">abstract submission on EasyChair</a> or emailed to the <a href="committee.html">organising committee</a>.</p>
    </div>
  </article>
</section>
'''
page("speakers.html", "Keynote speakers", speakers, "Keynote speakers at the CDT in AI Annual Conference 2026, including Prof. James Brusey of Coventry University.")

# ---------------------------------------------------------------- REVIEWERS
commit = [("Confidentiality", "Submissions are confidential. Do not share, discuss or reuse their content outside the review process."),
          ("Conflicts of interest", "Decline any abstract by your own supervisor, supervisee, close collaborator or research group, or where you cannot be impartial. Tell the committee and it will be reassigned."),
          ("Constructive tone", "Write the review you would want to receive. Be specific, be respectful and suggest improvements. Many authors are first-year researchers."),
          ("Timeliness", "Return reviews by the deadline so authors can be notified on 25 September."),
          ("Your own judgement", "Reviews should reflect your own expert reading of the abstract. Do not share submissions with third parties or external tools.")]
criteria = [("Relevance to the conference and topic", "Does the work engage with artificial intelligence, and does it fit the topic selected by the author?"),
            ("Clarity of the abstract", "Are the problem, approach and contribution stated clearly within the 250-word limit? Could a researcher from another discipline follow it?"),
            ("Methodological rigour", "Is the method appropriate and described adequately for its stage? For early work, is the plan sound and are the claims proportionate?"),
            ("Originality and contribution", "Does the work offer something new: a method, an application, a finding, a critical perspective or a new interdisciplinary link?"),
            ("Impact and responsible practice", "Is the potential academic, industrial or societal impact articulated? Are ethical, governance or bias considerations acknowledged where relevant?")]
scale = [("5", "Excellent, no concerns"), ("4", "Good, minor issues"), ("3", "Acceptable, some weaknesses"), ("2", "Weak, significant concerns"), ("1", "Poor, does not meet the criterion")]
recs = [("Accept as paper presentation", "Strong, mature work suited to a 20-minute talk"), ("Accept as lightning talk", "Clear, focused idea or early-stage work suited to 5 minutes"),
        ("Accept as poster", "Suitable for discussion at the poster exhibition"), ("Reject", "Out of scope or does not meet the minimum standard; explain why")]
reviewers = page_head("Reviewers", "Call for reviewers",
                      "Peer review keeps the programme strong and is valuable experience for early-career researchers. Reviewing runs from 19 to 24 September 2026.") + f'''
<section class="wrap section two-col">
  <div>
    <h2 class="h2-small">How it works</h2>
    <p class="body-2" style="margin-bottom:22px;max-width:48ch">We invite CDT in AI students, supervisors and staff to review abstracts submitted to the conference. Each reviewer receives a small number of abstracts matched to their expertise, and reviews are completed on EasyChair.</p>
    <ol class="mini-dates">
      <li data-date="2026-09-18T23:59:00"><span class="stamp mono-date">18 SEP</span><span>Submissions close and abstracts are allocated to reviewers</span></li>
      <li data-date="2026-09-24T23:59:00"><span class="stamp mono-date">24 SEP</span><span>Reviews due on EasyChair</span></li>
      <li data-date="2026-09-25T23:59:00"><span class="stamp mono-date">25 SEP</span><span>Committee decisions and author notification</span></li>
    </ol>
    <p class="body-2" style="margin-bottom:20px;max-width:48ch">To volunteer, answer <strong>“Yes”</strong> to “Are you happy to review papers?” on the registration form, or email the <a href="committee.html">organising committee</a>.</p>
    <a class="btn btn-gold" href="{REGISTER}">Volunteer via the registration form</a>
  </div>
  <div class="narrow">
    <h2 class="h2-small">What reviewers commit to</h2>
    <dl class="def">{"".join(f'<div><dt>{t}</dt><dd>{d}</dd></div>' for t, d in commit)}</dl>
  </div>
</section>

<section class="band section">
  <div class="wrap-inner">
    <div class="section-head"><h2>Review criteria</h2><p class="kicker">Score each 1 – 5</p></div>
    <div class="two-col">
      <ol class="criteria">{"".join(f'<li><span class="num">0{i}</span><div><p class="t">{t}</p><p class="d">{d}</p></div></li>' for i, (t, d) in enumerate(criteria, 1))}</ol>
      <div class="narrow">
        <p class="eyebrow sm">Scoring scale</p>
        <dl class="def ruled scale" style="margin-bottom:30px">{"".join(f'<div><dt>{s}</dt><dd>{d}</dd></div>' for s, d in scale)}</dl>
        <p class="eyebrow sm">Overall recommendation</p>
        <dl class="def ruled recs" style="margin-bottom:30px">{"".join(f'<div><dt>{t}</dt><dd>{d}</dd></div>' for t, d in recs)}</dl>
        <p class="eyebrow sm">Written comments</p>
        <p class="body-2" style="font-size:15px">Give two or three sentences for the authors: what is strong, what would most improve the work, and any format recommendation. Add a separate confidential note for the committee if needed. The committee makes final decisions on format and session allocation.</p>
      </div>
    </div>
  </div>
</section>
'''
page("reviewers.html", "Reviewers", reviewers, "Call for reviewers and review guidelines for the CDT in AI Annual Conference 2026.")

# ---------------------------------------------------------------- COMMITTEE
PEOPLE = [("Chair", "Adeola Eze", "ezea2@uni.coventry.ac.uk"), ("Deputy Chair", "Muhammed Khan", "khanm442@uni.coventry.ac.uk"), ("Deputy Chair", "Iqra Jilani", "jilanii@uni.coventry.ac.uk")]
committee = page_head("Committee", "Organising committee", "The conference is organised by postgraduate researchers of the Centre for Doctoral Training in AI.") + f'''
<section class="wrap section">
  <ul class="people">{"".join(f'<li><span class="role">{r}</span><span class="name">{n}</span><a href="mailto:{e}">{e}</a></li>' for r, n, e in PEOPLE)}</ul>
  <div class="two-col" style="margin-top:clamp(34px,4vw,52px)">
    <div>
      <h2 class="h2-plain">Programme committee</h2>
      <p class="body-2" style="max-width:48ch">Abstracts are reviewed by CDT in AI students, supervisors and staff who volunteer through the registration form. Reviewer names will be listed here after the review period, with their permission. <a href="reviewers.html">Join the programme committee.</a></p>
    </div>
    <div>
      <h2 class="h2-plain">Administrative contact</h2>
      <p class="body-2" style="max-width:48ch">For attendance queries, including if you are a CDT in AI student unable to attend, please email <a href="mailto:{RMAP}">{RMAP}</a>.</p>
    </div>
  </div>
</section>
'''
page("committee.html", "Committee", committee, "Organising committee for the CDT in AI Annual Conference 2026 at Coventry University.")

# ---------------------------------------------------------------- VENUE
venue = page_head("Venue", "Venue and travel", "Room EC1 29, Sir Frank Whittle Building, Coventry University, Gosford Street, Coventry CV1 5DL.") + f'''
<section class="wrap section two-col">
  <div>
    <dl class="def ruled inline" style="margin-bottom:26px">
      <div><dt>Room</dt><dd class="big">EC1 29</dd></div>
      <div><dt>Building</dt><dd>Sir Frank Whittle Building, Coventry University</dd></div>
      <div><dt>Address</dt><dd>Gosford Street, Coventry CV1 5DL, United Kingdom</dd></div>
      <div><dt>Doors</dt><dd>Registration from 09:00; follow signs to EC1 29 from the main entrance</dd></div>
    </dl>
    <p class="body-2" style="margin-bottom:10px;max-width:52ch">The Sir Frank Whittle Building is on the main city-centre campus, next to the Lanchester Library and the William Morris Building, and is recognisable by its hexagonal window frames.</p>
    <p class="muted" style="font-size:14.5px;margin-bottom:22px;max-width:52ch">The building also fronts Gulson Road; the main campus map lists it under Gosford Street.</p>
    <a class="btn btn-outline" href="https://www.google.com/maps/search/?api=1&amp;query=Sir+Frank+Whittle+Building+Coventry+University+CV1+5DL">Open in Google Maps</a>
    <div style="margin-top:clamp(28px,4vw,40px)">
      <h3 class="venue-h3">By train</h3>
      <p class="venue-p">Coventry railway station is a short walk, bus or taxi ride from the campus, with direct services from London, Birmingham and the wider West Midlands.</p>
      <h3 class="venue-h3">By car</h3>
      <p class="venue-p">Parking on campus is limited, so please use public city-centre car parks. Use the CV1 5DL postcode for navigation.</p>
      <h3 class="venue-h3">Access and dietary requirements</h3>
      <p class="venue-p" style="margin-bottom:0">Email <a href="mailto:{RMAP}">{RMAP}</a> so we can make arrangements.</p>
    </div>
  </div>
  <div class="narrow">
    <iframe class="map" title="Map showing the Sir Frank Whittle Building, Coventry University" loading="lazy" referrerpolicy="no-referrer-when-downgrade" src="https://www.openstreetmap.org/export/embed.html?bbox=-1.5040%2C52.4030%2C-1.4950%2C52.4080&amp;layer=mapnik&amp;marker=52.4053%2C-1.4996"></iframe>
    <p class="map-link"><a href="https://www.openstreetmap.org/?mlat=52.4053&amp;mlon=-1.4996#map=17/52.4053/-1.4996">View larger map on OpenStreetMap ↗</a></p>
    <div class="callout"><p class="eyebrow">On the day</p><p>Registration opens at 09:00 in EC1 29. Lunch and refreshments are provided. Photography and recording will take place during the event; consent is requested on the registration form.</p></div>
    <p style="margin-top:22px">{CAL_BTN}</p>
  </div>
</section>
'''
page("venue.html", "Venue", venue, "Venue and travel information for the CDT in AI Annual Conference 2026: EC1 29, Sir Frank Whittle Building, Coventry University, CV1 5DL.")

# ---------------------------------------------------------------- CONTACT
contact = page_head("Contact", "Get in touch", "Questions about submissions, reviewing, attendance or the programme.") + f'''
<section class="wrap section two-col">
  <div>
    <p class="label-rule">Submissions and programme</p>
    <ul class="contact-list">{"".join(f'<li><p class="name">{n} <span>· {r}</span></p><a href="mailto:{e}">{e}</a></li>' for r, n, e in PEOPLE)}</ul>
  </div>
  <div class="narrow">
    <p class="label-rule">Attendance and catering</p>
    <p class="body-2" style="margin-bottom:12px">For registration queries, dietary or access requirements, or to explain why you cannot attend.</p>
    <a class="small-link" href="mailto:{RMAP}">{RMAP}</a>
    <p class="label-rule spaced">Quick links</p>
    <ul class="links">
      <li><a href="{EASYCHAIR}">Submit an abstract on EasyChair ↗</a></li>
      <li><a href="{CFP_URL}">EasyChair call for papers ↗</a></li>
      <li><a href="{REGISTER}">Registration form (Microsoft Forms) ↗</a></li>
      <li><a href="reviewers.html">Call for reviewers</a></li>
    </ul>
  </div>
</section>
'''
page("contact.html", "Contact", contact, "Contact the organisers of the CDT in AI Annual Conference 2026, Coventry University.")
