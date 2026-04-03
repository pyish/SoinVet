document.addEventListener("DOMContentLoaded", function () {
    // Function to open a modal
    function openModal(modalId) {
      const modal = document.getElementById(modalId);
      if (modal) {
        modal.style.display = "block";
        document.body.classList.add("modal-open"); // Prevent scrolling
      }
    }
  
    // Function to destroy (remove) a modal and clean up
    function destroyModal(modalId) {
      const modal = document.getElementById(modalId);
      if (modal) {
        modal.parentNode.removeChild(modal); // Remove modal from DOM
        document.body.classList.remove("modal-open"); // Allow scrolling again
      }
    }
  
    // Event delegation for opening modals
    document.addEventListener("click", function (e) {
      if (e.target.matches("[data-modal-open]")) {
        const modalId = e.target.getAttribute("data-modal-open");
        openModal(modalId);
      }
    });
  
    // Event delegation for closing and destroying modals
    document.addEventListener("click", function (e) {
      if (e.target.matches("[data-modal-close]")) {
        const modalId = e.target.getAttribute("data-modal-close");
        destroyModal(modalId);
      }
    });
  
    // Close and destroy modal when clicking outside the modal content
    document.addEventListener("click", function (e) {
      const modals = document.querySelectorAll(".modal");
      modals.forEach((modal) => {
        if (e.target === modal) {
          destroyModal(modal.id);
        }
      });
    });
  });