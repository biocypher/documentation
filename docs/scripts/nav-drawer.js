/**
 * Mobile drawer: open at the top navigation level.
 *
 * Material marks the active nav trail's toggles as `checked`, which on mobile
 * pre-drills the drawer into the active product. Reset those toggles whenever
 * the drawer opens so it always starts at the product list. The drawer is only
 * interactive below the tabs breakpoint, so desktop sidebar expansion (which
 * relies on the same `checked` state) is unaffected.
 */
(function () {
  var drawer = document.getElementById("__drawer");
  if (!drawer) return;

  drawer.addEventListener("change", function () {
    if (!drawer.checked) return;
    document
      .querySelectorAll(".md-nav--primary .md-nav__toggle")
      .forEach(function (toggle) {
        toggle.checked = false;
      });
  });
})();
