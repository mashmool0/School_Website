let checker = false;
function clickChecker(){
  if(checker==false){
    document.querySelector(".HamburgerMenu").style.backgroundColor = "rgba(0, 0, 0, 0.4)";
    let links = document.querySelectorAll(".SideLinks a");
    
    for(let a=0 ; a<links.length ; a++){
      links[a].style.display = "block";
    }
    checker= true;
  }

  else{
    
    document.querySelector(".HamburgerMenu").style.background = "none";
    let links = document.querySelectorAll(".SideLinks a");
    for(let a=0 ; a<links.length ; a++){
      links[a].style.display = "none";
    }
    checker = false;
  }
}