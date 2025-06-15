// Initialize AOS library
// AOS.init({
//   duration: 800,
//   easing: "ease-in-out",
//   once: true,
// });

// // Preloader
// window.addEventListener("load", function () {
//   const preloader = document.querySelector(".preloader");
//   preloader.classList.add("fade-out");
//   setTimeout(function () {
//     preloader.style.display = "none";
//   }, 500);
// });

// Navbar scroll effect
window.addEventListener("scroll", function () {
  const nav = document.querySelector("nav");
  if (window.scrollY > 100) {
    nav.classList.add("scrolled");
  } else {
    nav.classList.remove("scrolled");
  }

  // Back to top button
  const backToTop = document.querySelector(".back-to-top");
  if (window.scrollY > 300) {
    backToTop.classList.add("active");
  } else {
    backToTop.classList.remove("active");
  }
});

// Mobile menu toggle
function clickChecker() {
  const sideLinks = document.querySelector(".SideLinks");
  const burgerInput = document.getElementById("burger");

  if (burgerInput.checked) {
    sideLinks.classList.add("active");
  } else {
    sideLinks.classList.remove("active");
  }
}

// Back to top functionality
document.querySelector(".back-to-top").addEventListener("click", function () {
  window.scrollTo({
    top: 0,
    behavior: "smooth",
  });
});

// Redirect functions
function redirectToLogin() {
  window.location.href = "{% url 'account:login' %}";
}

function redirectTo_panel() {
  window.location.href = "{% url 'panel:lastOrder' %}";
}
