var arr=[];
while (true) {
  var strt=prompt("Do u want to start?");
  if(strt=="Y"){
  var inputP=prompt("Commands: Add Display Remove or Quit?");

   if(inputP=="Q"){
      alert("Thanks for visiting the site. visit again");
      break;
    }
 else if (inputP=="A" ) {
var n=prompt("Enter a name");
arr.push(n);
  }
  else if (inputP=="D" ) {
    console.log(arr);
  }
  else if (inputP=="R") {
    if(arr.length==0){
    alert("There is no element here");
    continue;}
  var n=prompt("Please enter a name");
  var t=arr.indexOf(n);
  arr.splice(t,1);
  }
}
else {
  break;
}
}
