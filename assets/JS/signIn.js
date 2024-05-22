let obj = [{email:"mfsdjkn@gmail.con" , code:"20498552"}]
function checker(){
  const email = document.getElementById('email').value;
  const code = document.getElementById('code').value;
  // // console.log(code+email);
  // for(let i=0 ; i<obj.length ;i++){
  //   // console.log("1");
  //   if(email==obj.email&&obj.code == code){
  //   }
  //   return;
  // }
  let danger = document.getElementById("danger");
  danger.className="danger";
  // console.log("!");
}
document.getElementById('submit').onclick=function(){
  checker();
}