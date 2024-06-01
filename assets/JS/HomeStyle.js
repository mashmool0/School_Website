let checker = false;
function clickChecker(){
  if(checker==false){
    document.querySelector(".HamburgerMenu").style.backgroundColor = "rgba(0, 0, 0, 0.6)";
    let links = document.querySelectorAll(".SideLinks a");
    
    for(let a=0 ; a<links.length ; a++){
      links[a].style.display = "block";
    }
    document.querySelector(".cards").style.zIndex = "-1"
    document.querySelector(".headerContent").style.zIndex = "-1"
    checker= true;
  }

  else{
    
    document.querySelector(".HamburgerMenu").style.background = "none";
    let links = document.querySelectorAll(".SideLinks a");
    for(let a=0 ; a<links.length ; a++){
      links[a].style.display = "none";
    }
    document.querySelector(".cards").style.zIndex = "0"
    document.querySelector(".headerContent").style.zIndex = "0"
    checker = false;
  }
}