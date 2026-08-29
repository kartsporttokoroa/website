// Tokoroa Kart Club — shared site behaviour
document.addEventListener('DOMContentLoaded', function () {
  var toggle = document.querySelector('.nav-toggle');
  var nav = document.querySelector('.main-nav');

  if (toggle && nav) {
    toggle.addEventListener('click', function () {
      nav.classList.toggle('is-open');
      var expanded = nav.classList.contains('is-open');
      toggle.setAttribute('aria-expanded', expanded ? 'true' : 'false');
    });
  }

  // Close mobile nav when a link is clicked
  document.querySelectorAll('.main-nav a').forEach(function (link) {
    link.addEventListener('click', function () {
      if (nav) nav.classList.remove('is-open');
    });
  });

  // Footer year
  var yearEl = document.getElementById('year');
  if (yearEl) yearEl.textContent = new Date().getFullYear();
});
