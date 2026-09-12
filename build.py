#!/usr/bin/env python3
"""Generates the static HTML pages from one shared header/footer template.
Edit content in this file, then run `python3 build.py` and commit the HTML.
No dependencies beyond Python 3."""
from pathlib import Path

SITE = "CDT in AI Annual Conference 2026"
EASYCHAIR = "https://easychair.org/conferences/?conf=cdtinaiannualconfere0"
CFP_URL = "https://easychair.org/cfp/coventryuniversitycdtinai2026"
REGISTER = "https://forms.cloud.microsoft/Pages/ResponsePage.aspx?id=mqsYS2U3vkqsfA4NOYr9Txeve1SJEVJCqEbhUMPBqIZUQTRKRkpRMDQ3NTI3MjNDT1paQ0gyVUE4WC4u"
RMAP = "RMAP.Science@coventry.ac.uk"

NAV = [
    ("index.html", "Home"),
    ("call-for-papers.html", "Call for Papers"),
    ("programme.html", "Programme"),
    ("speakers.html", "Keynotes"),
    ("reviewers.html", "Reviewers"),
    ("committee.html", "Committee"),
    ("venue.html", "Venue"),
    ("contact.html", "Contact"),
]

def header(active):
    items = "".join(
        f'<li><a href="{href}"{" aria-current=\"page\"" if href == active else ""}>{label}</a></li>'
        for href, label in NAV)
    return f'''<a class="skip-link" href="#main">Skip to content</a>
<header class="site-header">
  <div class="container">
    <a class="brand" href="index.html">
      <img src="assets/img/logo.png" alt="Coventry University Centre for Doctoral Training in AI logo">
      <div><strong>CDT in AI Conference 2026</strong><span>Coventry University</span></div>
    </a>
    <button class="nav-toggle" aria-expanded="false" aria-controls="site-nav">Menu</button>
    <nav class="site-nav" id="site-nav" aria-label="Main navigation"><ul>{items}</ul></nav>
  </div>
</header>'''

FOOTER = f'''<footer class="site-footer">
  <div class="container">
    <div>
      <a class="brand" href="index.html"><img src="assets/img/logo.png" alt=""><div><strong>CDT in AI Annual Conference 2026</strong><span>Coventry University</span></div></a>
      <p style="margin-top:14px">Artificial Intelligence across Domains: Research, Innovation and Impact.<br>Wednesday 7 October 2026 · EC1 29, Sir Frank Whittle Building, Coventry University.</p>
    </div>
    <div>
      <h4>Take part</h4>
      <ul>
        <li><a href="{EASYCHAIR}">Submit on EasyChair</a></li>
        <li><a href="{REGISTER}">Register to attend</a></li>
        <li><a href="reviewers.html">Become a reviewer</a></li>
      </ul>
    </div>
    <div>
      <h4>Contact</h4>
      <ul>
        <li><a href="mailto:{RMAP}">{RMAP}</a></li>
        <li><a href="committee.html">Organising committee</a></li>
        <li><a href="venue.html">Getting here</a></li>
      </ul>
    </div>
  </div>
  <p class="copyright">© 2026 Centre for Doctoral Training in AI, Coventry University.</p>
</footer>
<script src="assets/js/main.js"></script>'''

def page(filename, title, body, description):
    html = f'''<!DOCTYPE html>
<html lang="en-GB">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title} · {SITE}</title>
<meta name="description" content="{description}">
<link rel="icon" type="image/png" href="assets/img/favicon.png">
<link rel="stylesheet" href="assets/css/style.css">
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

def banner(eyebrow, h1, text):
    return f'''<section class="page-banner"><div class="container">
  <p class="eyebrow">{eyebrow}</p><h1>{h1}</h1><p>{text}</p>
</div></section>'''

# ---------------------------------------------------------------- HOME
home = f'''
<section class="hero">
  <div class="container">
    <div>
      <p class="eyebrow">Coventry University · Centre for Doctoral Training in AI</p>
      <h1>Artificial Intelligence Across Domains</h1>
      <p class="subtitle">Research, Innovation and Impact</p>
      <p class="lead">A one-day conference showcasing the diverse research being undertaken by postgraduate researchers at Coventry University whose work engages with artificial intelligence.</p>
      <div class="hero-meta">
        <div><strong>Date</strong>Wednesday 7 October 2026</div>
        <div><strong>Time</strong>09:00 – 16:30 · registration from 09:00</div>
        <div><strong>Venue</strong>EC1 29, Sir Frank Whittle Building</div>
        <div><strong>Countdown</strong><span id="countdown">7 October 2026</span></div>
      </div>
      <div class="btn-row">
        <a class="btn btn-gold" href="{EASYCHAIR}">Submit an abstract</a>
        <a class="btn btn-outline" href="{REGISTER}">Register to attend</a>
        <a class="btn btn-outline" href="programme.html">View programme</a>
      </div>
    </div>
    <img src="assets/img/logo.png" alt="CDT in AI phoenix emblem">
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="notice"><strong>Abstracts close Friday 18 September 2026.</strong> Submit a 250-word abstract and 100-word biography via EasyChair. Notification of outcome by 25 September 2026. <a href="call-for-papers.html">Read the full call for papers.</a></div>
    <h2 style="margin-top:28px">Ways to take part</h2>
    <div class="grid grid-3">
      <div class="card"><div class="big">20 min</div><h3>Paper presentations</h3><p>Full-length talks in the midday and afternoon panels, each followed by Q&amp;A.</p></div>
      <div class="card"><div class="big">5 min</div><h3>Lightning talks</h3><p>Short, focused talks in two blocks, well suited to work in its early stages.</p></div>
      <div class="card"><div class="big">All day</div><h3>Poster presentations</h3><p>On display from lunch through the closing session, with authors alongside. Awards presented at 15:45.</p></div>
    </div>
  </div>
</section>

<section class="section alt">
  <div class="container">
    <div class="section-head"><p class="eyebrow">Themes</p><h2>Four topic areas</h2><p>Submissions are invited across every discipline in which AI plays a part. Choose the topic that best fits your work when you submit.</p></div>
    <div class="grid grid-2">
      <div class="card"><h3>AI Research, Innovation, Methods, Models and Applications</h3><p>New algorithms, architectures, learning methods, evaluation and applied systems.</p></div>
      <div class="card"><h3>AI across Disciplines and Professional Contexts</h3><p>AI in engineering, health, business, the arts, education, law and other professional domains.</p></div>
      <div class="card"><h3>Responsible AI: Ethics, Governance, Transparency, Bias and Trust</h3><p>Fairness, accountability, explainability, regulation and public trust.</p></div>
      <div class="card"><h3>Generative AI: Knowledge, Human Experience and Societal Impact</h3><p>Large language and multimodal models, creativity, knowledge work and society.</p></div>
    </div>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="grid grid-2">
      <div>
        <p class="eyebrow">Keynote</p>
        <h2>Prof. James Brusey</h2>
        <p>Professor of Computer Science at Coventry University and lead of the Human-Centred Reinforcement Learning theme at the Research Centre for Computational Science and Mathematical Modelling. Keynote 10:00 – 10:40, followed by Q&amp;A until 11:00.</p>
        <p><a class="btn btn-navy" href="speakers.html">Meet the keynote speakers</a></p>
      </div>
      <div>
        <p class="eyebrow">Who should attend</p>
        <h2>Open to CDT in AI postgraduate researchers</h2>
        <p>The conference is open to Coventry University CDT in AI postgraduate researchers across all disciplines, along with supervisors and staff members of the CDT. All CDT in AI students are expected to attend and to contribute a talk, poster or paper.</p>
        <p><a class="btn btn-navy" href="{REGISTER}">Register now</a></p>
      </div>
    </div>
  </div>
</section>
'''
page("index.html", "Home", home, "CDT in AI Annual Conference 2026, Coventry University. Artificial Intelligence across Domains: Research, Innovation and Impact. Wednesday 7 October 2026.")

# ---------------------------------------------------------------- CALL FOR PAPERS
cfp = banner("Call for Papers", "Call for Participation",
             "Abstracts are invited for paper presentations, lightning talks and posters from Coventry University CDT in AI postgraduate researchers across all disciplines.") + f'''
<section class="section">
  <div class="container">
    <div class="grid grid-2" style="align-items:start">
      <div>
        <h2>About the conference</h2>
        <p>The CDT in AI Annual Conference 2026, <em>Artificial Intelligence across Domains: Research, Innovation and Impact</em>, is a one-day conference showcasing the diverse research being undertaken by postgraduate researchers within Coventry University whose work engages with artificial intelligence.</p>
        <p>It takes place on <strong>Wednesday 7 October 2026</strong> in <strong>EC1 29, Sir Frank Whittle Building, Coventry University</strong>. Participation is open to Coventry University CDT in AI postgraduate researchers across all disciplines. All CDT in AI students are expected to attend and to contribute.</p>
        <h2 style="margin-top:32px">Topics</h2>
        <p>Submissions are welcome in any area where AI plays a part. Please select one of the four topics on EasyChair:</p>
        <ol>
          <li><strong>AI Research, Innovation, Methods, Models and Applications</strong></li>
          <li><strong>AI across Disciplines and Professional Contexts</strong></li>
          <li><strong>Responsible AI: Ethics, Governance, Transparency, Bias and Trust</strong></li>
          <li><strong>Generative AI: Knowledge, Human Experience and Societal Impact</strong></li>
        </ol>
      </div>
      <div>
        <h2>Important dates</h2>
        <ul class="dates">
          <li data-date="2026-09-18"><time>18 September 2026</time><div><strong>Abstract registration and submission deadline</strong><br>Friday, via EasyChair</div></li>
          <li data-date="2026-09-25"><time>25 September 2026</time><div><strong>Notification of outcome</strong><br>Authors informed by email</div></li>
          <li data-date="2026-10-07"><time>7 October 2026</time><div><strong>Conference day</strong><br>09:00 – 16:30, EC1 29, Sir Frank Whittle Building</div></li>
        </ul>
        <div class="notice" style="margin-top:20px"><strong>Registration to attend</strong> is separate from abstract submission. <a href="{REGISTER}">Complete the registration form</a> even if you are not presenting.</div>
      </div>
    </div>
  </div>
</section>

<section class="section alt">
  <div class="container">
    <div class="section-head"><p class="eyebrow">Formats</p><h2>Presentation formats</h2><p>Choose the format that best suits the stage of your work. Session chairs will keep time, and speakers should load their slides during the preceding break.</p></div>
    <div class="grid grid-3">
      <div class="card"><div class="big">20 min</div><h3>Paper presentation</h3><p>Full-length talks in the midday and afternoon panels (Panel 1 at 11:15 and Panel 2 at 14:00), each followed by Q&amp;A. Suited to mature work with results.</p></div>
      <div class="card"><div class="big">5 min</div><h3>Lightning talk</h3><p>Short, focused talks in two blocks (12:30 and 15:15) with Q&amp;A. Well suited to work in its early stages or a single key idea.</p></div>
      <div class="card"><div class="big">All day</div><h3>Poster presentation</h3><p>On display from lunch (13:00) through the closing session, with authors alongside. Poster awards are presented at 15:45. All first-year CDT in AI students present a poster.</p></div>
    </div>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="grid grid-2" style="align-items:start">
      <div>
        <h2>How to submit</h2>
        <ol>
          <li>Go to the <a href="{EASYCHAIR}">EasyChair submission page</a> and sign in or create a free EasyChair account.</li>
          <li>Enter your <strong>abstract (250 words maximum)</strong> and a <strong>short biography (100 words maximum)</strong>.</li>
          <li>Select your preferred format: paper presentation, lightning talk or poster.</li>
          <li>Select one of the four topics.</li>
          <li>Submit before <strong>Friday 18 September 2026</strong>. You can edit your submission on EasyChair until the deadline.</li>
        </ol>
        <p>Suggestions for the second keynote speaker are welcome and can be sent alongside your abstract submission.</p>
        <div class="btn-row">
          <a class="btn btn-gold" href="{EASYCHAIR}">Submit on EasyChair</a>
          <a class="btn btn-navy" href="{CFP_URL}">EasyChair call for papers</a>
        </div>
      </div>
      <div>
        <h2>Review and selection</h2>
        <p>Every abstract is reviewed by members of the CDT in AI community against the published <a href="reviewers.html">review criteria</a>: relevance, clarity, rigour, originality and impact. Authors are notified of the outcome, and of their allocated format and session, by <strong>25 September 2026</strong>.</p>
        <p>There are twelve presentation slots in total: six 20-minute paper presentations and six 5-minute lightning talks, plus the poster exhibition. Where demand exceeds the slots available, the committee may offer an alternative format.</p>
        <p>Want to help review? See the <a href="reviewers.html">call for reviewers</a>.</p>
      </div>
    </div>
  </div>
</section>

<section class="section alt">
  <div class="container">
    <div class="poster-wrap">
      <a href="assets/img/poster.png"><img src="assets/img/poster.png" alt="Call for Participation poster for the CDT in AI Conference 2026"></a>
      <div>
        <p class="eyebrow">Share the call</p>
        <h2>Call for Participation poster</h2>
        <p>Download and share the poster with colleagues in your research centre. The QR code links to the EasyChair submission page.</p>
        <p><a class="btn btn-navy" href="assets/img/poster.png">Open poster image</a></p>
      </div>
    </div>
  </div>
</section>
'''
page("call-for-papers.html", "Call for Papers", cfp, "Call for papers and important dates for the CDT in AI Annual Conference 2026 at Coventry University. Abstracts due 18 September 2026.")

# ---------------------------------------------------------------- PROGRAMME
def row(t, what, sub="", cls=""):
    c = f' class="{cls}"' if cls else ""
    s = f"<small>{sub}</small>" if sub else ""
    return f"<tr{c}><td class=\"time\">{t}</td><td>{what}{s}</td></tr>"

morning = "".join([
    row("09:00 – 09:30", "Registration", "", "break"),
    row("09:30 – 10:00", "Welcome and introductions"),
    row("10:00 – 10:40", "Keynote: Prof. James Brusey", "Professor of Computer Science, Coventry University", "highlight"),
    row("10:40 – 11:00", "Keynote Q&amp;A"),
    row("11:00 – 11:15", "Break", "", "break"),
    row("11:15 – 12:15", "Panel 1", "Three 20-minute paper presentations and Q&amp;A"),
    row("12:15 – 12:30", "Break", "", "break"),
])
afternoon = "".join([
    row("12:30 – 13:00", "Lightning talks 1", "Three 5-minute talks and Q&amp;A"),
    row("13:00 – 14:00", "Lunch", "Poster exhibition opens", "break"),
    row("14:00 – 15:00", "Panel 2", "Three 20-minute paper presentations and Q&amp;A"),
    row("15:00 – 15:15", "Break", "", "break"),
    row("15:15 – 15:45", "Lightning talks 2", "Three 5-minute talks and Q&amp;A"),
    row("15:45 – 16:30", "End note and awards", "Networking and poster exhibition", "highlight"),
])
def slots(title, time, kind):
    return f'''<div class="card"><h3>{title}</h3><p class="eyebrow" style="margin:0">{time}</p><ol><li>Presenter TBC</li><li>Presenter TBC</li><li>Presenter TBC</li></ol><small>{kind}</small></div>'''

programme = banner("Programme", "Running order",
                   "Wednesday 7 October 2026 · 09:00 – 16:30 · EC1 29, Sir Frank Whittle Building. Provisional until presenters are confirmed after 25 September.") + f'''
<section class="section">
  <div class="container">
    <div class="notice">The programme is provisional. Presenter names and the second keynote session will be added once submissions are reviewed. Session chairs will keep time; please load your slides during the preceding break.</div>
    <div class="grid grid-2" style="align-items:start;margin-top:24px">
      <div><h2>Morning · 09:00 – 12:30</h2><div class="table-wrap"><table class="schedule"><thead><tr><th>Time</th><th>Session</th></tr></thead><tbody>{morning}</tbody></table></div></div>
      <div><h2>Midday and afternoon · 12:30 – 16:30</h2><div class="table-wrap"><table class="schedule"><thead><tr><th>Time</th><th>Session</th></tr></thead><tbody>{afternoon}</tbody></table></div></div>
    </div>
  </div>
</section>
<section class="section alt">
  <div class="container">
    <div class="section-head"><p class="eyebrow">Twelve presentation slots</p><h2>Sessions at a glance</h2></div>
    <div class="slots">
      {slots("Panel 1", "11:15 – 12:15", "20-minute papers, then Q&amp;A")}
      {slots("Lightning 1", "12:30 – 13:00", "5-minute talks, then Q&amp;A")}
      {slots("Panel 2", "14:00 – 15:00", "20-minute papers, then Q&amp;A")}
      {slots("Lightning 2", "15:15 – 15:45", "5-minute talks, then Q&amp;A")}
    </div>
    <p style="margin-top:20px">Posters are on display from 13:00 through the closing session, with awards presented at 15:45.</p>
  </div>
</section>
'''
page("programme.html", "Programme", programme, "Running order for the CDT in AI Annual Conference 2026: keynote, panels, lightning talks, poster exhibition and awards.")

# ---------------------------------------------------------------- SPEAKERS
speakers = banner("Keynotes", "Keynote speakers", "Two keynote sessions anchor the day. The second speaker will be announced ahead of the full programme.") + f'''
<section class="section">
  <div class="container">
    <div class="card" style="margin-bottom:24px">
      <div class="speaker">
        <div class="avatar" aria-hidden="true">JB</div>
        <div>
          <span class="pill gold">Keynote 1 of 2 · 10:00 – 10:40</span>
          <h2 style="margin-top:10px">Prof. James Brusey</h2>
          <p><strong>Professor of Computer Science, Coventry University, United Kingdom</strong></p>
          <p>Leads the Human-Centred Reinforcement Learning theme at Coventry University's Research Centre for Computational Science and Mathematical Modelling. His research spans machine learning, reinforcement learning and AI for cyber-physical systems, with industry projects involving JLR, Rolls-Royce and Orbit Group.</p>
          <p>Appointed Innovate UK BridgeAI Independent Scientific Advisor at The Alan Turing Institute in 2025.</p>
          <ul class="stats"><li>20+ PhD graduates</li><li>25 grants secured</li><li>£35M in research funding</li></ul>
          <p style="margin-top:14px">Keynote 10:00 – 10:40, followed by Q&amp;A until 11:00.</p>
        </div>
      </div>
    </div>
    <div class="card">
      <div class="speaker">
        <div class="avatar tba" aria-hidden="true">To be<br>announced</div>
        <div>
          <span class="pill">Keynote 2 of 2 · time to be confirmed</span>
          <h2 style="margin-top:10px">Second keynote speaker</h2>
          <p>Our second keynote will be confirmed ahead of the full programme's publication, and announced to registered attendees by email.</p>
          <p>Suggestions from CDT in AI supervisors and researchers are welcome. Nominations can be sent alongside your <a href="{EASYCHAIR}">abstract submission on EasyChair</a> or emailed to the <a href="committee.html">organising committee</a>.</p>
        </div>
      </div>
    </div>
  </div>
</section>
'''
page("speakers.html", "Keynote speakers", speakers, "Keynote speakers at the CDT in AI Annual Conference 2026, including Prof. James Brusey of Coventry University.")

# ---------------------------------------------------------------- REVIEWERS
reviewers = banner("Reviewers", "Call for reviewers and review guidelines",
                   "Peer review keeps the programme strong and is a valuable experience for early-career researchers. Reviewing runs from 19 to 24 September 2026.") + f'''
<section class="section">
  <div class="container">
    <div class="grid grid-2" style="align-items:start">
      <div>
        <h2>Call for reviewers</h2>
        <p>We invite CDT in AI students, supervisors and staff to review abstracts submitted to the conference. Each reviewer receives a small number of abstracts matched to their expertise, and reviews are completed on EasyChair.</p>
        <ul class="dates">
          <li data-date="2026-09-18"><time>18 September</time><div>Submissions close and abstracts are allocated to reviewers</div></li>
          <li data-date="2026-09-24"><time>24 September</time><div>Reviews due on EasyChair</div></li>
          <li data-date="2026-09-25"><time>25 September</time><div>Committee decisions and author notification</div></li>
        </ul>
        <p style="margin-top:18px">To volunteer, answer <strong>“Yes”</strong> to “Are you happy to review papers?” on the registration form, or email the <a href="committee.html">organising committee</a>.</p>
        <a class="btn btn-gold" href="{REGISTER}">Volunteer via the registration form</a>
      </div>
      <div>
        <h2>What reviewers commit to</h2>
        <ul class="criteria">
          <li><strong>Confidentiality</strong>Submissions are confidential. Do not share, discuss or reuse their content outside the review process.</li>
          <li><strong>Conflicts of interest</strong>Decline any abstract by your own supervisor, supervisee, close collaborator or research group, or where you cannot be impartial. Tell the committee and it will be reassigned.</li>
          <li><strong>Constructive tone</strong>Write the review you would want to receive. Be specific, be respectful and suggest improvements. Many authors are first-year researchers.</li>
          <li><strong>Timeliness</strong>Return reviews by the deadline so authors can be notified on 25 September.</li>
          <li><strong>Your own judgement</strong>Reviews should reflect your own expert reading of the abstract. Do not share submissions with third parties or external tools.</li>
        </ul>
      </div>
    </div>
  </div>
</section>

<section class="section alt">
  <div class="container">
    <div class="section-head"><p class="eyebrow">Guidelines</p><h2>Review criteria</h2><p>Score each abstract on the five criteria below using the 1 to 5 scale, then give an overall recommendation and a short written comment for the authors.</p></div>
    <div class="grid grid-2" style="align-items:start">
      <ul class="criteria">
        <li><strong>1. Relevance to the conference and topic</strong>Does the work engage with artificial intelligence, and does it fit the topic selected by the author?</li>
        <li><strong>2. Clarity of the abstract</strong>Are the problem, approach and contribution stated clearly within the 250-word limit? Could a researcher from another discipline follow it?</li>
        <li><strong>3. Methodological rigour</strong>Is the method appropriate and described adequately for its stage? For early work, is the plan sound and are the claims proportionate?</li>
        <li><strong>4. Originality and contribution</strong>Does the work offer something new: a method, an application, a finding, a critical perspective or a new interdisciplinary link?</li>
        <li><strong>5. Impact and responsible practice</strong>Is the potential academic, industrial or societal impact articulated? Are ethical, governance or bias considerations acknowledged where relevant?</li>
      </ul>
      <div>
        <h3>Scoring scale</h3>
        <table class="scale">
          <thead><tr><th>Score</th><th>Meaning</th></tr></thead>
          <tbody>
            <tr><td>5</td><td>Excellent, no concerns</td></tr>
            <tr><td>4</td><td>Good, minor issues</td></tr>
            <tr><td>3</td><td>Acceptable, some weaknesses</td></tr>
            <tr><td>2</td><td>Weak, significant concerns</td></tr>
            <tr><td>1</td><td>Poor, does not meet the criterion</td></tr>
          </tbody>
        </table>
        <h3 style="margin-top:24px">Overall recommendation</h3>
        <table class="scale">
          <tbody>
            <tr><td><strong>Accept as paper presentation</strong></td><td>Strong, mature work suited to a 20-minute talk</td></tr>
            <tr><td><strong>Accept as lightning talk</strong></td><td>Clear, focused idea or early-stage work suited to 5 minutes</td></tr>
            <tr><td><strong>Accept as poster</strong></td><td>Suitable for discussion at the poster exhibition</td></tr>
            <tr><td><strong>Reject</strong></td><td>Out of scope or does not meet the minimum standard; explain why</td></tr>
          </tbody>
        </table>
        <h3 style="margin-top:24px">Written comments</h3>
        <p>Give two or three sentences for the authors: what is strong, what would most improve the work, and any format recommendation. Add a separate confidential note for the committee if needed. The committee makes final decisions on format and session allocation.</p>
      </div>
    </div>
  </div>
</section>
'''
page("reviewers.html", "Reviewers", reviewers, "Call for reviewers and review guidelines for the CDT in AI Annual Conference 2026.")

# ---------------------------------------------------------------- COMMITTEE
def person(initials, name, role, email):
    return f'''<div class="card"><div class="person"><div class="avatar" aria-hidden="true">{initials}</div><div><strong>{name}</strong><span>{role}</span><a href="mailto:{email}">{email}</a></div></div></div>'''
committee = banner("Committee", "Organising committee", "The conference is organised by postgraduate researchers of the Centre for Doctoral Training in AI.") + f'''
<section class="section">
  <div class="container">
    <div class="grid grid-3">
      {person("AE", "Adeola Eze", "Conference Chair", "ezea2@uni.coventry.ac.uk")}
      {person("IJ", "Iqra Jilani", "Deputy Chair", "jilanii@uni.coventry.ac.uk")}
      {person("MK", "Muhammed Khan", "Deputy Chair", "khanm442@uni.coventry.ac.uk")}
    </div>
    <div class="grid grid-2" style="margin-top:32px;align-items:start">
      <div>
        <h2>Programme committee</h2>
        <p>Abstracts are reviewed by CDT in AI students, supervisors and staff who volunteer through the registration form. Reviewer names will be listed here after the review period, with their permission. <a href="reviewers.html">Join the programme committee.</a></p>
      </div>
      <div>
        <h2>Administrative contact</h2>
        <p>For attendance queries, including if you are a CDT in AI student unable to attend, please email <a href="mailto:{RMAP}">{RMAP}</a>.</p>
      </div>
    </div>
  </div>
</section>
'''
page("committee.html", "Committee", committee, "Organising committee for the CDT in AI Annual Conference 2026 at Coventry University.")

# ---------------------------------------------------------------- VENUE
venue = banner("Venue", "Getting to the conference", "Room EC1 29, Sir Frank Whittle Building, Coventry University, Gosford Street, Coventry CV1 5DL.") + f'''
<section class="section">
  <div class="container">
    <div class="grid grid-2" style="align-items:start">
      <div>
        <h2>Venue</h2>
        <p><strong>Room EC1 29</strong><br>Sir Frank Whittle Building<br>Coventry University<br>Gosford Street<br>Coventry CV1 5DL<br>United Kingdom</p>
        <p style="font-size:.9rem;color:var(--ink-soft)">The building also fronts Gulson Road; the main campus map lists it under Gosford Street.</p>
        <p>The Sir Frank Whittle Building is on the main city-centre campus, next to the Lanchester Library and the William Morris Building, and is recognisable by its hexagonal window frames. Follow signs to EC1 29 from the main entrance on the day.</p>
        <p><a class="btn btn-navy" href="https://www.google.com/maps/search/?api=1&query=Sir+Frank+Whittle+Building+Coventry+University+CV1+5DL">Open in Google Maps</a></p>
        <h3 style="margin-top:28px">By train</h3>
        <p>Coventry railway station is a short walk, bus or taxi ride from the campus, with direct services from London, Birmingham and the wider West Midlands.</p>
        <h3>By car</h3>
        <p>Parking on campus is limited, so please use public city-centre car parks. Use the CV1 5DL postcode for navigation.</p>
        <h3>Accessibility</h3>
        <p>If you have access or dietary requirements, please email <a href="mailto:{RMAP}">{RMAP}</a> so we can make arrangements.</p>
      </div>
      <div>
        <iframe class="map" title="Map showing the Sir Frank Whittle Building, Coventry University" loading="lazy" referrerpolicy="no-referrer-when-downgrade" src="https://www.openstreetmap.org/export/embed.html?bbox=-1.5040%2C52.4030%2C-1.4950%2C52.4080&amp;layer=mapnik&amp;marker=52.4053%2C-1.4996"></iframe>
        <p style="font-size:.85rem;color:var(--ink-soft);margin-top:8px"><a href="https://www.openstreetmap.org/?mlat=52.4053&amp;mlon=-1.4996#map=17/52.4053/-1.4996">View larger map on OpenStreetMap</a></p>
        <div class="notice"><strong>On the day</strong><br>Registration opens at 09:00 in EC1 29. Lunch and refreshments are provided. Photography and recording will take place during the event; consent is requested on the form.</div>
      </div>
    </div>
  </div>
</section>
'''
page("venue.html", "Venue", venue, "Venue and travel information for the CDT in AI Annual Conference 2026: EC1 29, Sir Frank Whittle Building, Coventry University, CV1 5DL.")

# ---------------------------------------------------------------- CONTACT
contact = banner("Contact", "Get in touch", "Questions about submissions, reviewing, attendance or the programme.") + f'''
<section class="section">
  <div class="container">
    <div class="grid grid-3">
      <div class="card"><h3>Submissions and programme</h3><p>Contact the organising committee.</p><ul style="padding-left:1.1em"><li>Adeola Eze, Chair<br><a href="mailto:ezea2@uni.coventry.ac.uk">ezea2@uni.coventry.ac.uk</a></li><li>Iqra Jilani, Deputy Chair<br><a href="mailto:jilanii@uni.coventry.ac.uk">jilanii@uni.coventry.ac.uk</a></li><li>Muhammed Khan, Deputy Chair<br><a href="mailto:khanm442@uni.coventry.ac.uk">khanm442@uni.coventry.ac.uk</a></li></ul></div>
      <div class="card"><h3>Attendance and catering</h3><p>For registration queries, dietary or access requirements, or to explain why you cannot attend.</p><p><a href="mailto:{RMAP}">{RMAP}</a></p></div>
      <div class="card"><h3>Quick links</h3><ul style="padding-left:1.1em"><li><a href="{EASYCHAIR}">Submit an abstract on EasyChair</a></li><li><a href="{CFP_URL}">EasyChair call for papers</a></li><li><a href="{REGISTER}">Registration form (Microsoft Forms)</a></li><li><a href="reviewers.html">Call for reviewers</a></li></ul></div>
    </div>
  </div>
</section>
'''
page("contact.html", "Contact", contact, "Contact the organisers of the CDT in AI Annual Conference 2026, Coventry University.")
