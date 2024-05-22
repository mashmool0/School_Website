let checker = false;
function clickChecker(){
  if(checker==false){
    document.querySelector(".HamburgerMenu").style.backgroundColor = "rgba(0, 0, 0, 0.4)";
    let links = document.querySelectorAll(".SideLinks a");
    
    for(let a=0 ; a<links.length ; a++){
      links[a].style.display = "block";
    }
  }
  else{
    
    document.querySelector(".HamburgerMenu").style.background = "none";
    document.querySelectorAll(".SideLinks a").style.display = "none";
  }
}