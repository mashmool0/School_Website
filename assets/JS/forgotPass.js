var container = document.getElementsByClassName("number")[0];
container.onkeyup = function (e) {
  var target = e.srcElement;
  var maxLength = parseInt(target.attributes["maxlength"].value, 10);
  var myLength = target.value.length;
  if (myLength >= maxLength) {
    var next = target;
    while ((next = next.nextElementSibling)) {
      if (next == null) break;
      if (next.tagName.toLowerCase() == "input") {
        next.focus();
        break;
      }
    }
  }
};
var container = document.getElementsByClassName("number")[1];
container.onkeyup = function (e) {
  var target = e.srcElement;
  var maxLength = parseInt(target.attributes["maxlength"].value, 10);
  var myLength = target.value.length;
  if (myLength >= maxLength) {
    var next = target;
    while ((next = next.nextElementSibling)) {
      if (next == null) break;
      if (next.tagName.toLowerCase() == "input") {
        next.focus();
        break;
      }
    }
  }
};
var container = document.getElementsByClassName("number")[2];
container.onkeyup = function (e) {
  var target = e.srcElement;
  var maxLength = parseInt(target.attributes["maxlength"].value, 10);
  var myLength = target.value.length;
  if (myLength >= maxLength) {
    var next = target;
    while ((next = next.nextElementSibling)) {
      if (next == null) break;
      if (next.tagName.toLowerCase() == "input") {
        next.focus();
        break;
      }
    }
  }
};
let checker = false;
function clickChecker() {
  if (checker == false) {
    document.querySelector(".HamburgerMenu").style.backgroundColor =
      "rgba(0, 0, 0, 0.4)";
    let links = document.querySelectorAll(".SideLinks a");
    for (let a = 0; a < links.length; a++) {
      links[a].style.display = "block";
    }
    checker = true;
    document.getElementById("forgotPass").style.zIndex = "-1";
  } else {
    document.querySelector(".HamburgerMenu").style.background = "none";
    let links = document.querySelectorAll(".SideLinks a");
    for (let a = 0; a < links.length; a++) {
      links[a].style.display = "none";
    }
    checker = false;
    document.getElementById("forgotPass").style.zIndex = "1";
  }
}
