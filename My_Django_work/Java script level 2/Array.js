var arr=["A","B","C"];
console.log(arr);
arr[0]="D";
var last=arr.pop();
arr.push("New Item");
console.log(arr.length);
var matrix=[[1,2,3],[4,5,6],[7,8,9]];
var mixed=[1,true,"String"];

for (var i = 0; i < arr.length; i++) {
console.log(arr[i]);
}
for(lettr of arr){
  console.log(lettr);
}
// for (var i = 0; i < arr.length; i++) {
//   alert(arr[i]);
// }
///This will do the same work as the loop
console.log(arr.forEach(alert));

function eachforfun(name) {
  console.log("Its awesome  "+name);
}

var topics=["Python","Django","Java Script"];
topics.forEach(eachforfun);
mixed.pop("true");
console.log(mixed);
