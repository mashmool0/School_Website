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
document.querySelector(".SecondSlide button").addEventListener("click" , function(){
  
  if(document.querySelector(".FirstSlide").previousElementSibling == undefined){
    console.log("null")
  }
  document.querySelector(".FirstSlide").previousElementSibling.setAttribute('class' , 'slide FirstSlide');
  document.querySelectorAll(".FirstSlide")[1].setAttribute('class' , 'slide')
  document.querySelector(".SecondSlide").previousElementSibling.setAttribute('class' , 'slide SecondSlide');
  document.querySelectorAll(".SecondSlide")[1].setAttribute('class' ,'SecondSlide');
  document.querySelector(".ThirdSlide").previousElementSibling.setAttribute('class' , ' slide ThirdSlide');
  document.querySelectorAll(".ThirdSlide")[1].setAttribute("class" , 'slide');
})