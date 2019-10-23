var emp={name:"john",
job:"programmer",
age:31,
           myMethod:function() {

             console.log("The myMethod was called "+this.name.lenght);
           },
           methodAlert:function(){
             alert("Name is "+this.name);
             alert("Job is "+this.job);
             alert("Age is "+this.age);
           },
           lastName:function(){
   console.log(this.name.split(" ")[1]);
 }
           }
           
