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
