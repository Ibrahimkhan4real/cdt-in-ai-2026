// CDT in AI Annual Conference 2026 — behaviour ported from the design file's Component logic.
(function () {
  var CONF_START = new Date('2026-10-07T09:00:00');
  var CONF_END = new Date('2026-10-07T16:30:00');
  var DEADLINE = new Date('2026-09-18T23:59:00');

  // Programme rows. cls: "break" | "gold" (highlighted). tag: right-hand label.
  var SCHEDULE = [
    { time: "09:00 – 09:30", title: "Registration", detail: "Tea, coffee and badges in EC1 29", cls: "break" },
    { time: "09:30 – 10:00", title: "Welcome and introductions", detail: "Organising committee" },
    { time: "10:00 – 10:40", title: "Keynote: Prof. James Brusey", detail: "Professor of Computer Science, Coventry University", cls: "gold", tag: "Keynote" },
    { time: "10:40 – 11:00", title: "Keynote Q&A", detail: "Open floor, chaired" },
    { time: "11:00 – 11:15", title: "Break", cls: "break" },
    { time: "11:15 – 12:15", title: "Panel 1", detail: "Three 20-minute paper presentations and Q&A", tag: "Papers" },
    { time: "12:15 – 12:30", title: "Break", cls: "break" },
    { time: "12:30 – 13:00", title: "Lightning talks 1", detail: "Three 5-minute talks and Q&A", tag: "Lightning" },
    { time: "13:00 – 14:00", title: "Lunch", detail: "Poster exhibition opens", cls: "break", tag: "Posters" },
    { time: "14:00 – 15:00", title: "Panel 2", detail: "Three 20-minute paper presentations and Q&A", tag: "Papers" },
    { time: "15:00 – 15:15", title: "Break", cls: "break" },
    { time: "15:15 – 15:45", title: "Lightning talks 2", detail: "Three 5-minute talks and Q&A", tag: "Lightning" },
    { time: "15:45 – 16:30", title: "End note and awards", detail: "Networking and poster exhibition", cls: "gold", tag: "Awards" }
  ];

  var now = new Date();
  function daysUntil(target) { return Math.ceil((target - now) / 86400000); }
  function countdown(n, words) { return n > 1 ? n + ' ' + words.plural : n === 1 ? words.one : n === 0 ? words.zero : words.past; }
  function esc(s) { return String(s == null ? '' : s).replace(/&/g, '&amp;').replace(/</g, '&lt;'); }
  function icsUtc(d) { return d.toISOString().replace(/[-:]/g, '').replace(/\.\d{3}Z$/, 'Z'); }

  // Mobile navigation
  var toggle = document.querySelector('.nav-toggle');
  var nav = document.querySelector('.site-nav');
  if (toggle && nav) {
    toggle.addEventListener('click', function () {
      var open = nav.classList.toggle('open');
      toggle.setAttribute('aria-expanded', open ? 'true' : 'false');
    });
  }

  // Countdowns: live, ticking every second as "24d 13h 05m 42s" (the days part drops below a day)
  var dD = daysUntil(DEADLINE);
  var confEls = document.querySelectorAll('[data-conference-countdown]');
  var deadlineEls = document.querySelectorAll('[data-deadline-countdown]');
  function pad(n) { return (n < 10 ? '0' : '') + n; }
  function formatRemaining(ms) {
    var t = Math.max(0, Math.floor(ms / 1000));
    var d = Math.floor(t / 86400), h = Math.floor((t % 86400) / 3600), m = Math.floor((t % 3600) / 60), s = t % 60;
    return (d > 0 ? d + 'd ' : '') + pad(h) + 'h ' + pad(m) + 'm ' + pad(s) + 's';
  }
  function tick() {
    var t = new Date();
    var confText, confLabel = '';
    if (t >= CONF_END) confText = 'Thank you for joining us';
    else if (t.toDateString() === CONF_START.toDateString()) confText = 'Today';
    else { confText = formatRemaining(CONF_START - t); confLabel = 'to go'; }
    confEls.forEach(function (el) {
      var digits = el.querySelector('.cd-digits'), label = el.querySelector('.cd-label');
      (digits || el).textContent = confText;
      if (label) label.textContent = confLabel;
    });
    var deadlineText = t > DEADLINE ? 'Submissions closed'
      : t.toDateString() === DEADLINE.toDateString() ? 'Closes today'
      : formatRemaining(DEADLINE - t) + ' left';
    deadlineEls.forEach(function (el) { el.textContent = deadlineText; });
  }
  tick();
  setInterval(tick, 1000);

  // Dates lists: grey out past items and fill the live status
  document.querySelectorAll('[data-date]').forEach(function (li) {
    var status = li.querySelector('.status');
    if (new Date(li.getAttribute('data-date')) < now) {
      li.classList.add('past');
      if (status) status.textContent = 'Passed';
    } else if (status && li.hasAttribute('data-deadline-status')) {
      status.textContent = countdown(dD, { plural: 'days left', one: 'Tomorrow', zero: 'Today', past: 'Closed' });
    }
  });

  // Add to calendar (.ics)
  function addToCalendar(e) {
    if (e) e.preventDefault();
    var lines = [
      "BEGIN:VCALENDAR", "VERSION:2.0", "PRODID:-//CDT in AI//Conference 2026//EN",
      "CALSCALE:GREGORIAN", "METHOD:PUBLISH", "BEGIN:VEVENT",
      "UID:cdt-in-ai-conference-2026@coventry.ac.uk",
      "DTSTAMP:20260101T000000Z",
      "DTSTART:" + icsUtc(CONF_START),
      "DTEND:" + icsUtc(CONF_END),
      "SUMMARY:CDT in AI Annual Conference 2026",
      "DESCRIPTION:Artificial Intelligence across Domains: Research\\, Innovation and Impact. Registration from 09:00.",
      "LOCATION:EC1 29\\, Sir Frank Whittle Building\\, Coventry University\\, Gosford Street\\, Coventry CV1 5DL",
      "END:VEVENT", "END:VCALENDAR"
    ];
    var blob = new Blob([lines.join("\r\n")], { type: "text/calendar;charset=utf-8" });
    var a = document.createElement("a");
    a.href = URL.createObjectURL(blob);
    a.download = "cdt-in-ai-conference-2026.ics";
    document.body.appendChild(a); a.click(); a.remove();
    setTimeout(function () { URL.revokeObjectURL(a.href); }, 2000);
  }
  document.querySelectorAll('[data-add-to-calendar]').forEach(function (b) { b.addEventListener('click', addToCalendar); });

  // Day-of mode: highlight the current session, only on the conference day itself
  var dayOf = now.toDateString() === CONF_START.toDateString();
  var nowIdx = -1;
  if (dayOf) {
    var nowMin = now.getHours() * 60 + now.getMinutes();
    var mins = function (t) { var p = t.split(':'); return p[0] * 60 + +p[1]; };
    nowIdx = SCHEDULE.findIndex(function (r) {
      var range = r.time.split(' – ');
      return nowMin >= mins(range[0]) && nowMin < mins(range[1]);
    });
    if (nowIdx === -1) nowIdx = nowMin < mins(SCHEDULE[0].time.split(' – ')[0]) ? 0 : SCHEDULE.length - 1;
    var bar = document.getElementById('now-bar');
    if (bar) {
      bar.hidden = false;
      bar.querySelector('.session').textContent = SCHEDULE[nowIdx].title;
      var next = SCHEDULE[nowIdx + 1];
      bar.querySelector('.next').textContent = 'Next · ' + (next ? next.time + ' ' + next.title : 'End of day');
    }
  }

  // Programme: timeline (default) and table views rendered from SCHEDULE
  var rows = SCHEDULE.map(function (r, i) {
    var live = dayOf && i === nowIdx;
    return { time: r.time, title: r.title, detail: r.detail || '', cls: live ? 'live' : (r.cls || ''), tag: live ? 'Now' : (r.tag || '') };
  });
  var tl = document.getElementById('timeline');
  if (tl) {
    tl.innerHTML = rows.map(function (r) {
      return '<li class="' + r.cls + '"><span class="time">' + esc(r.time) + '</span><div class="body"><p class="title">' + esc(r.title) + '</p>' +
        (r.detail ? '<p class="detail">' + esc(r.detail) + '</p>' : '') + '</div><span class="tag">' + esc(r.tag) + '</span></li>';
    }).join('');
  }
  var tbody = document.getElementById('schedule-body');
  if (tbody) {
    tbody.innerHTML = rows.map(function (r) {
      return '<tr class="' + r.cls + '"><td class="time">' + esc(r.time) + '</td><td class="title">' + esc(r.title) + '</td><td class="detail">' + esc(r.detail) + '</td></tr>';
    }).join('');
  }
  var views = document.querySelectorAll('.view-toggle button');
  views.forEach(function (b) {
    b.addEventListener('click', function () {
      var which = b.getAttribute('data-view');
      views.forEach(function (x) { x.setAttribute('aria-pressed', x === b ? 'true' : 'false'); });
      document.getElementById('view-timeline').hidden = which !== 'timeline';
      document.getElementById('view-table').hidden = which !== 'table';
    });
  });
})();
