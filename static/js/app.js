// Enable popovers everywhere
var popoverTriggerList = [].slice.call(
  document.querySelectorAll('[data-bs-toggle="popover"]')
);

var popoverList = popoverTriggerList.map(function (popoverTriggerEl) {
  return new bootstrap.Popover(popoverTriggerEl);
});

// Allow buttons elements in popovers
var allowList = bootstrap.Popover.Default.allowList;
allowList.button = ["data-bs-toggle", "data-bs-target", "class"];
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

// Adds back keyboard triggering to popover triggers
document.addEventListener('keydown', function(event) {
  const elem = event.target;
  if (elem.matches('.popover-trigger')) {
    if (event.code === "Space") elem.dispatchEvent(new Event("click"));
  }
});

// React to changes on provision checkboxes
document.addEventListener('change', function(event) {
  const elem = event.target;
  if (elem.matches('.provision-item > input[type="checkbox"]')) {
    adjustProvisionList(elem.dataset.text, elem.id, elem.checked);
  }
});

// Adds or removes provision list items.
function adjustProvisionList(text, id, add) {
  const provisionList = document.getElementById("provisions-list");
  const provisionSubmit = document.getElementById("provision-form-submit");

  if (add) {
    // Only add item if it's not already in the list
    if (!document.getElementById(`submit-${id}`)) {
      // Create <li>
      const item = document.createElement("li");
      item.id = `submit-${id}`;
      item.innerText = text;
      // Create encapsulated hidden input
      const itemData = document.createElement("input");
      itemData.name = "provisions";
      itemData.type = "hidden";
      itemData.value = id;
      item.appendChild(itemData);
      // create delete button
      const itemDelete = document.createElement("button");
      itemDelete.innerText = "X";
      itemDelete.addEventListener("click", (e) => {
        e.preventDefault();
        e.stopPropagation();
        // uncheck checkbox element in accordian for deleted provision
        const checkboxElem = document.getElementById(id);
        checkboxElem.checked = false;
        // remove parent li element
        adjustProvisionList(null, id, false);
      });
      itemDelete.classList.add("btn");
      itemDelete.classList.add("btn-outline-danger");
      itemDelete.classList.add("btn-sm");
      item.appendChild(itemDelete);
      // Append li element to ul
      provisionList.appendChild(item);
    }
  } else {
    // Remove item if unchecked
    provisionList.removeChild(document.getElementById(`submit-${id}`));
  }
  // If there are items in the list, submit button should be enabled
  provisionSubmit.disabled = !(provisionList.getElementsByTagName("li").length > 0);
}
