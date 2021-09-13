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
allowList.input = ["type", "name", "id", "data-text"];
allowList.label = ["for"]
allowList.li = ["data-id", "id"];

 /* Hides other popovers on show - bit of a hack but best I can do for now
    Ideally we should trigger popovers manually and have node effects toggled
    with classes rather than focus. Then we can target the classes for showing
    or hiding the popovers. List as "if we have time". */
popoverList.forEach(function (popover) {
  // Attach show event to each trigger
  popover._element.addEventListener('show.bs.popover', function(e) {
    // If a popover is being shown, hide all others.
    popoverList.forEach((item) => {if (item != popover) item.hide();});
  });
});

// React to changes on provision checkboxes
document.addEventListener('change', function(event) {
  const elem = event.target;
  if (elem.matches('.provision-item > input[type="checkbox"]')) {
    adjustProvisionList(elem.dataset.text, elem.id, elem.checked);
  }
});

// Adds or removes provision list items. TODO: Add a delete button to items.
function adjustProvisionList(text, id, add) {
  const provisionList = document.getElementById("provisions-list");

  if (add) {
    if (!document.getElementById(`submit-${id}`)) {
      const item = document.createElement("li");
      item.id = `submit-${id}`;
      item.innerText = text;
      provisionList.appendChild(item);
    }
  } else {
    provisionList.removeChild(document.getElementById(`submit-${id}`));
  }
}
