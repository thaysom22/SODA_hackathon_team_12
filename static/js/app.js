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
allowList.input = ["type", "name", "id", "data-title", "data-description"];
allowList.label = ["for"];
allowList.li = ["data-id", "id"];

/* Hides other popovers on show - bit of a hack but best I can do for now
    Ideally we should trigger popovers manually and have node effects toggled
    with classes rather than focus. Then we can target the classes for showing
    or hiding the popovers. List as "if we have time". */
popoverList.forEach(function (popover) {
  // Attach show event to each trigger
  popover._element.addEventListener("show.bs.popover", function (e) {
    // If a popover is being shown, hide all others.
    popoverList.forEach((item) => {
      if (item != popover) item.hide();
    });
  });
});

// Adds back keyboard triggering to popover triggers
document.addEventListener("keydown", function (event) {
  const elem = event.target;
  if (elem.matches(".popover-trigger")) {
    if (event.code === "Space") elem.dispatchEvent(new Event("click"));
  }
});

// React to changes on provision checkboxes
document.addEventListener("change", function (event) {
  const elem = event.target;
  if (elem.matches('.provision-item > input[type="checkbox"]')) {
    adjustProvisionList(
      elem.dataset.title,
      elem.dataset.description,
      elem.id,
      elem.checked
    );
  }
});

// Adds or removes provision list items. TODO: Add a delete button to items.
function adjustProvisionList(title, description, id, add) {
  const provisionList = document.getElementById("provisions-list");
  const provisionSubmit = document.getElementById("provision-form-submit");

  if (add) {
    // Only add item if it's not already in the list
    if (!document.getElementById(`submit-${id}`)) {
      // Create <li>
      const container = document.createElement("div");
      container.classList = "container text-start";
      container.id = `submit-${id}`;
      const item = document.createElement("div");
      item.innerHTML = `
      <dl class="row ">
        <dt class="col-sm-3">${title}</dt>
        <dd class="col-sm-9">${description}</dd>
      </dl>
      `;
      // Create encapsulated hidden input
      const itemData = document.createElement("input");
      itemData.name = "provisions";
      itemData.type = "hidden";
      itemData.value = id;
      item.appendChild(itemData);
      // Append to list
      provisionList.appendChild(container);
      container.appendChild(item);
    }
  } else {
    // Remove item if unchecked
    provisionList.removeChild(document.getElementById(`submit-${id}`));
  }
  // If there are items in the list, submit button should be enabled
  provisionSubmit.disabled = !(
    provisionList.getElementsByTagName("dl").length > 0
  );
}
