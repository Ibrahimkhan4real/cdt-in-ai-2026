// CDT in AI Annual Conference 2026 — behaviour ported from the design file's Component logic.
(function () {
  var CONF_START = new Date('2026-10-07T09:00:00');
  var DEADLINE = new Date('2026-09-18T23:59:00');

  var SCHEDULE = [
    ["09:00 – 09:30", "Registration", "Tea, coffee and badges in EC1 29", "break", ""],
    ["09:30 – 10:00", "Welcome and introductions", "Organising committee", "", ""],
    ["10:00 – 10:40", "Keynote: Prof. James Brusey", "Professor of Computer Science, Coventry University", "gold", "Keynote"],
    ["10:40 – 11:00", "Keynote Q&A", "Open floor, chaired", "", ""],
    ["11:00 – 11:15", "Break", "", "break", ""],
    ["11:15 – 12:15", "Panel 1", "Three 20-minute paper presentations and Q&A", "", "Papers"],
    ["12:15 – 12:30", "Break", "", "break", ""],
    ["12:30 – 13:00", "Lightning talks 1", "Three 5-minute talks and Q&A", "", "Lightning"],
    ["13:00 – 14:00", "Lunch", "Poster exhibition opens", "break", "Posters"],
    ["14:00 – 15:00", "Panel 2", "Three 20-minute paper presentations and Q&A", "", "Papers"],
    ["15:00 – 15:15", "Break", "", "break", ""],
    ["15:15 – 15:45", "Lightning talks 2", "Three 5-minute talks and Q&A", "", "Lightning"],
    ["15:45 – 16:30", "End note and awards", "Networking and poster exhibition", "gold", "Awards"]
  ];

  function days(target) { return Math.ceil((target - new Date()) / 86400000); }
  function esc(s) { return String(s).replace(/&/g, '&amp;').replace(/</g, '&lt;'); }

  // Mobile navigation
  var toggle = document.querySelector('.nav-toggle');
  var nav = document.querySelector('.site-nav');
  if (toggle && nav) {
    toggle.addEventListener('click', function () {
      var open = nav.classList.toggle('open');
      toggle.setAttribute('aria-expanded', open ? 'true' : 'false');
    });
  }

  // Countdowns
  var dD = days(DEADLINE);
  var dC = days(CONF_START);
  var deadlineText = dD > 1 ? dD + ' days left' : dD === 1 ? 'Closes tomorrow' : dD === 0 ? 'Closes today' : 'Submissions closed';
  var confText = dC > 1 ? dC + ' days to go' : dC === 1 ? 'Tomorrow' : dC === 0 ? 'Today' : 'Thank you for joining us';
  document.querySelectorAll('[data-deadline-countdown]').forEach(function (el) { el.textContent = deadlineText; });
  document.querySelectorAll('[data-conference-countdown]').forEach(function (el) { el.textContent = confText; });

  // Dates lists: mark past items and fill the live status
  var now = new Date();
  document.querySelectorAll('[data-date]').forEach(function (li) {
    var d = new Date(li.getAttribute('data-date'));
    var status = li.querySelector('.status');
    if (d < now) {
      li.classList.add('past');
      if (status) status.textContent = 'Passed';
    } else if (status && li.hasAttribute('data-deadline-status')) {
      status.textContent = dD > 1 ? dD + ' days left' : dD === 1 ? 'Tomorrow' : dD === 0 ? 'Today' : 'Closed';
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
      "DTSTART:20261007T080000Z",
      "DTEND:20261007T153000Z",
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

  // Day-of mode: on only during the conference day itself
  var dayOf = now.getFullYear() === 2026 && now.getMonth() === 9 && now.getDate() === 7;
  var nowIdx = -1;
  if (dayOf) {
    var nowMin = now.getHours() * 60 + now.getMinutes();
    var mins = function (t) { var p = t.split(':').map(Number); return p[0] * 60 + p[1]; };
    for (var i = 0; i < SCHEDULE.length; i++) {
      var parts = SCHEDULE[i][0].split(' – ');
      if (nowMin >= mins(parts[0]) && nowMin < mins(parts[1])) { nowIdx = i; break; }
    }
    if (nowIdx === -1) nowIdx = nowMin < mins(SCHEDULE[0][0].split(' – ')[0]) ? 0 : SCHEDULE.length - 1;
    var bar = document.getElementById('now-bar');
    if (bar) {
      bar.hidden = false;
      bar.querySelector('.session').textContent = SCHEDULE[nowIdx][1];
      var nx = SCHEDULE[nowIdx + 1];
      bar.querySelector('.next').textContent = 'Next · ' + (nx ? nx[0] + ' ' + nx[1] : 'End of day');
    }
  }

  // Programme: timeline (default) and table views rendered from SCHEDULE
  var tl = document.getElementById('timeline');
  var tbody = document.getElementById('schedule-body');
  if (tl) {
    tl.innerHTML = SCHEDULE.map(function (r, i) {
      var live = dayOf && i === nowIdx;
      var cls = live ? 'live' : r[3];
      var tag = live ? 'Now' : r[4];
      return '<li class="' + cls + '"><span class="time">' + esc(r[0]) + '</span><div class="body"><p class="title">' + esc(r[1]) + '</p>' +
        (r[2] ? '<p class="detail">' + esc(r[2]) + '</p>' : '') + '</div><span class="tag">' + esc(tag) + '</span></li>';
    }).join('');
  }
  if (tbody) {
    tbody.innerHTML = SCHEDULE.map(function (r, i) {
      var live = dayOf && i === nowIdx;
      return '<tr class="' + (live ? 'live' : r[3]) + '"><td class="time">' + esc(r[0]) + '</td><td class="title">' + esc(r[1]) + '</td><td class="detail">' + esc(r[2]) + '</td></tr>';
    }).join('');
  }
  var views = document.querySelectorAll('.view-toggle button');
  views.forEach(function (b) {
    b.addEventListener('click', function () {
      views.forEach(function (x) { x.setAttribute('aria-pressed', x === b ? 'true' : 'false'); });
      var which = b.getAttribute('data-view');
      document.getElementById('view-timeline').hidden = which !== 'timeline';
      document.getElementById('view-table').hidden = which !== 'table';
    });
  });
})();
