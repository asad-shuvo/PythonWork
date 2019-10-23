var carInfo={model:"Toyota",year:1990};
console.log(carInfo);

myNewO={a:"hello",b:[1,2,3],c:{inside:['a','b','c']}};
console.log(myNewO["c"]["inside"][1]);///Output b
//mutable
carInfo['year']=2006;

for(key in carInfo){
  // no specifin order
  console.log(key);//It will show us the key
  // If we want to see value
  console.log(carInfo[key]);
}
 // object method
 var sample={prop:"Hello",
            myMethod:function() {
              console.log("The myMethod was called");
            }
            }
var sampleName={name:"shuvo",
                       myMethodName:function() {
                         console.log("Name is "+this.name);
                       }
                       }
