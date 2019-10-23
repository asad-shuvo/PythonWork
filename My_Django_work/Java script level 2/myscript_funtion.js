function hello(name){
  console.log("Hello World "+name);
}

function addNum(num1,num2) {
  console.log(num1+num2);
}

function helloSomeOne(name="Frank"){
  console.log(name);
}
function fomal(name="sam",title="sir") {
  return title+"  "+name;
}

function timesFive(numInput) {
  var result=numInput*5;
  return result;

}

var v="Gloval v";
var stuff="Gloval Stuff";
function fun(stuff) {
  console.log(v);
  stuff="Reassign stuff inside func";
  console.log(stuff);
}
