var one=document.querySelector("#one");
var two=document.querySelector("#two");
var three=document.querySelector("#three");
var four=document.querySelector("#four");
var five=document.querySelector("#five");
var six=document.querySelector("#six");
var seven=document.querySelector("#seven");
var eight=document.querySelector("#eight");
var nine=document.querySelector("#nine");
var Restart=document.querySelector('#b');

Restart.addEventListener('click',function() {
  one.textContent=1;
  two.textContent=2;
  three.textContent=3;
  four.textContent=4;
  five.textContent=5;
  six.textContent=6;
  seven.textContent=7;
  eight.textContent=8;
  nine.textContent=9;

})

one.addEventListener("click",function() {
if(one.textContent==1){
  one.textContent="X";
}
else if(one.textContent=="X"){
one.textContent="O";
}
else if(one.textContent=="O"){
one.textContent=1;
}
})

two.addEventListener("click",function() {
  if(two.textContent==2){
    two.textContent="X";
  }
  else if(two.textContent=="X"){
  two.textContent="O";
  }
  else if(two.textContent=="O"){
  two.textContent=2;
  }
})
three.addEventListener("click",function() {
  if(three.textContent==3){
    three.textContent="X";
  }
  else if(three.textContent=="X"){
  three.textContent="O";
  }
  else if(three.textContent=="O"){
  three.textContent=3;
  }
})
four.addEventListener("click",function() {
  if(four.textContent==4){
    four.textContent="X";
  }
  else if(four.textContent=="X"){
  four.textContent="O";
  }
  else if(four.textContent=="O"){
  four.textContent=4;
  }
})

five.addEventListener("click",function() {
  if(five.textContent==5){
    five.textContent="X";
  }
  else if(five.textContent=="X"){
  five.textContent="O";
  }
  else if(five.textContent=="O"){
  five.textContent=5;
  }
})

six.addEventListener("click",function() {
  if(six.textContent==6){
    six.textContent="X";
  }
  else if(six.textContent=="X"){
  six.textContent="O";
  }
  else if(six.textContent=="O"){
  six.textContent=6;
  }
})

seven.addEventListener("click",function() {
  if(seven.textContent==7){
    seven.textContent="X";
  }
  else if(seven.textContent=="X"){
  seven.textContent="O";
  }
  else if(seven.textContent=="O"){
  seven.textContent=7;
  }
})

eight.addEventListener("click",function() {
  if(eight.textContent==8){
    eight.textContent="X";
  }
  else if(eight.textContent=="X"){
  eight.textContent="O";
  }
  else if(eight.textContent=="O"){
  eight.textContent=8;
  }
})

nine.addEventListener("click",function() {
  if(nine.textContent==9){
    nine.textContent="X";
  }
  else if(nine.textContent=="X"){
  nine.textContent="O";
  }
  else if(nine.textContent=="O"){
  nine.textContent=9;
  }
})
