let dropCheck = false;

function dropdown() {
  const dropDownDivs = document.querySelectorAll(".dropDown div");
  const notif = document.querySelector(".notif");

  if (!dropCheck) {
    dropDownDivs.forEach((div) => {
      div.style.display = "block";
    });
    document.querySelector(".dropDown").style.marginTop = "120px";
    notif.style.marginTop = "120px";
    dropCheck = true;
  } else {
    dropDownDivs.forEach((div) => {
      div.style.display = "none";
    });
    document.querySelector(".dropDown").style.marginTop = "0";
    notif.style.marginTop = "0";
    dropCheck = false;
  }
}

let dropCheck2 = false;

function dropdown2() {
  const mobDivs = document.querySelectorAll(".mob div");

  if (!dropCheck2) {
    mobDivs.forEach((div) => {
      div.style.display = "block";
    });
    document.querySelector(".mob").style.marginTop = "120px";
    dropCheck2 = true;
  } else {
    mobDivs.forEach((div) => {
      div.style.display = "none";
    });
    document.querySelector(".mob").style.marginTop = "0";
    dropCheck2 = false;
  }
}
