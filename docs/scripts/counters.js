/**
 * Count-up animation for the landing-page impact stat band.
 *
 * Subscribes to Material's `document$` observable (same pattern as
 * scripts/tablesort.js) so it re-runs on every instant-navigation page load.
 * Progressive enhancement: the final value is already in the HTML, so if JS is
 * disabled or the element is off-screen the correct number still shows.
 */
document$.subscribe(function () {
  var nums = document.querySelectorAll(".tx-stat__num[data-count]");
  if (!nums.length) return;

  function animate(el) {
    var target = parseInt(el.getAttribute("data-count"), 10);
    var suffix = el.getAttribute("data-suffix") || "";
    if (isNaN(target)) return;

    var duration = 1100;
    var start = null;

    function step(ts) {
      if (start === null) start = ts;
      var progress = Math.min((ts - start) / duration, 1);
      // easeOutCubic
      var eased = 1 - Math.pow(1 - progress, 3);
      el.textContent = Math.round(eased * target) + suffix;
      if (progress < 1) requestAnimationFrame(step);
    }
    requestAnimationFrame(step);
  }

  if (!("IntersectionObserver" in window)) {
    nums.forEach(animate);
    return;
  }

  var observer = new IntersectionObserver(
    function (entries) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) {
          animate(entry.target);
          observer.unobserve(entry.target);
        }
      });
    },
    { threshold: 0.5 }
  );

  nums.forEach(function (el) {
    observer.observe(el);
  });
});
