let dropCheck = false;
function dropdown() {
  if (dropCheck == false) {
    let links = document.querySelectorAll(".dropDown div");
    for (let a = 0; a < links.length; a++) {
      links[a].style.display = "block";
    }
    document.querySelector(".dropDown").style.marginTop = "120px";
    document.querySelector(".notif").style.marginTop = "120px"
    dropCheck = true;
  } else {
    let links = document.querySelectorAll(".dropDown div");
    for (let a = 0; a < links.length; a++) {
      links[a].style.display = "none";
    }
    document.querySelector(".dropDown").style.marginTop = "0";
    document.querySelector(".notif").style.marginTop = "0"
    dropCheck = false;
  }
}
let dropCheck2 = false;
function dropdown2() {
  if (dropCheck2 == false) {
    let links = document.querySelectorAll(".mob div");
    for (let a = 0; a < links.length; a++) {
      links[a].style.display = "block";
    }
    document.querySelector(".mob").style.marginTop = "120px";
    dropCheck2 = true;
  } else {
    let links = document.querySelectorAll(".mob div");
    for (let a = 0; a < links.length; a++) {
      links[a].style.display = "none";
    }
    document.querySelector(".mob").style.marginTop = "0";
    dropCheck2 = false;
  }
}
plusBtn = document.querySelectorAll(".PlusBtn");
for(let i=0 ; i<plusBtn.length ; i++){
  plusBtn[i].addEventListener("click" , function(){
    if(plusBtn[i].nextElementSibling.style.display == "none"){
      plusBtn[i].nextElementSibling.style.display ="block"
    }
    else{
      p = plusBtn[i].nextElementSibling.innerHTML;
      plusBtn[i].nextElementSibling.innerHTML = ++p;
    }
  })
}

MinusBtn = document.querySelectorAll(".MinusBtn");
for(let i=0 ; i<MinusBtn.length ; i++){
  MinusBtn[i].addEventListener("click" , function(){
    p = plusBtn[i].nextElementSibling.innerHTML;
    if(p!=1){
      plusBtn[i].nextElementSibling.innerHTML = --p;
    }
    else if(p==1){
      plusBtn[i].nextElementSibling.style.display = "none";

    }
  })
}