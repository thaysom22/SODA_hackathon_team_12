// Enable popovers everywhere
var popoverTriggerList = [].slice.call(
  document.querySelectorAll('[data-bs-toggle="popover"]')
);

var popoverList = popoverTriggerList.map(function (popoverTriggerEl) {
  return new bootstrap.Popover(popoverTriggerEl);
});

// Allow buttons elements in popovers
var allowList = bootstrap.Popover.Default.allowList;
allowList.button = ["data-bs-toggle", "data-bs-target"];

 /* Hides other popovers on show - bit of a hack but best I can do for now
    Ideally we should trigger popovers manually and have node effects toggled
    with classes rather than focus. Then we can target the classes for showing
    or hiding the popovers. */
popoverList.forEach(function (popover) {
  // Attach show event to each trigger
  popover._element.addEventListener('show.bs.popover', function(e) {
    // If a popover is being shown, hide all others.
    popoverList.forEach((item) => {if (item != popover) item.hide();});
  });
});
