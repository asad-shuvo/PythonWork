
var firstname=prompt("What is your first name?");
var Lastname=prompt("What is your Last name?");
var age=prompt("What is your age?");
var height=prompt("What is your height?");
var pet=prompt("What is your pet name");
var bl=false;
if(pet[pet.length-1]==="y")bl=true;
 if((firstname[0]==Lastname[0]) && (age>=20 && age<=30) && (height>=170) && bl===true){
 console.log("You are welcome mate");
}
else {
  console.log("Denied");
}
