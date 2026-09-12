// Mobile navigation toggle and countdown
(function () {
  var toggle = document.querySelector('.nav-toggle');
  var nav = document.querySelector('.site-nav');
  if (toggle && nav) {
    toggle.addEventListener('click', function () {
      var open = nav.classList.toggle('open');
      toggle.setAttribute('aria-expanded', open ? 'true' : 'false');
    });
  }
  // Mark past dates on the Important Dates list
  var today = new Date(); today.setHours(0, 0, 0, 0);
  document.querySelectorAll('.dates li[data-date]').forEach(function (li) {
    var d = new Date(li.getAttribute('data-date') + 'T00:00:00');
    if (d < today) li.classList.add('past');
  });
  // Countdown to the conference
  var cd = document.getElementById('countdown');
  if (cd) {
    var conf = new Date('2026-10-07T09:00:00');
    var diff = Math.ceil((conf - new Date()) / 86400000);
    if (diff > 1) cd.textContent = diff + ' days to go';
    else if (diff === 1) cd.textContent = 'Tomorrow';
    else if (diff === 0) cd.textContent = 'Today';
    else cd.textContent = 'Thank you for joining us';
  }
})();
