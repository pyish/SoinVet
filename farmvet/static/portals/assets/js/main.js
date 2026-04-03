function dateFormater(value, row) {
  return moment(value).format('DD-MM-YYYY'); 
}

jQuery(function ($) {
  // Handle clicks on sidebar dropdown items
  $(".sidebar-dropdown > a").click(function (e) {
      e.preventDefault();

      var $submenu = $(this).next(".sidebar-submenu"); // Target the submenu directly below the clicked item
      var $parentDropdown = $(this).parent(".sidebar-dropdown"); // The parent dropdown of the clicked item

      // If this dropdown is already active, close it
      if ($parentDropdown.hasClass("active")) {
          $submenu.slideUp(200); // Close the submenu
          $parentDropdown.removeClass("active"); // Remove the active class
      } else {
          // Close all other open submenus at the same level
          $parentDropdown.siblings(".sidebar-dropdown").removeClass("active").find(".sidebar-submenu").slideUp(200);

          // Open the clicked submenu
          $submenu.slideDown(200); // Open the submenu
          $parentDropdown.addClass("active"); // Add active class to the clicked dropdown
      }
  });

  // Handle clicks to toggle the sidebar visibility
  $("#close-sidebar").click(function () {
      $(".page-wrapper").removeClass("toggled");
  });

  $("#show-sidebar").click(function () {
      $(".page-wrapper").addClass("toggled");
  });
});

    
  