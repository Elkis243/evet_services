// Loader functionality
window.addEventListener("load", function () {
  const loader = document.getElementById("loading");
  if (loader) {
    // Attendre un peu pour que l'animation soit visible
    setTimeout(function () {
      loader.classList.add("hidden");
      // Retirer complètement du DOM après la transition
      setTimeout(function () {
        loader.remove();
      }, 500);
    }, 500);
  }
});

// Fallback si la page charge très rapidement
document.addEventListener("DOMContentLoaded", function () {
  const loader = document.getElementById("loading");
  if (loader && document.readyState === "complete") {
    setTimeout(function () {
      loader.classList.add("hidden");
      setTimeout(function () {
        loader.remove();
      }, 500);
    }, 500);
  }
});

// Initialisation des autres fonctionnalités
document.addEventListener("DOMContentLoaded", function () {
  // Fermer le menu mobile Bootstrap collapse quand on clique sur un lien
  const navbarCollapse = document.getElementById("navbarNav");
  const navLinks = document.querySelectorAll("#navbarNav .nav-link");

  if (navbarCollapse && navLinks.length > 0) {
    navLinks.forEach(function (link) {
      link.addEventListener("click", function () {
        // Fermer le menu collapse si Bootstrap est disponible
        if (typeof bootstrap !== "undefined" && bootstrap.Collapse) {
          const bsCollapse = bootstrap.Collapse.getInstance(navbarCollapse);
          if (bsCollapse) {
            bsCollapse.hide();
          }
        }
      });
    });
  }

  // Initialiser sal.js
  if (typeof sal !== "undefined") {
    sal({
      threshold: 0.1,
      once: false,
      easing: "ease-in-out",
    });
  }
});

