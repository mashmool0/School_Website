let checker = false;
function clickChecker(){
  if(checker==false){
    document.querySelector(".HamburgerMenu").style.backgroundColor = "rgba(0, 0, 0, 0.6)";
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
btn = document.querySelectorAll(".button");

btn.forEach(elem => {
  elem.addEventListener("click" , function(){
    btn.forEach(newElem=>{
      newElem.removeAttribute('id');
    })
    elem.setAttribute('id' , 'active');
  })
});