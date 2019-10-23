function sleepIn(weekday,vacation) {
  if(weekday==false && vacation==false)
  return true;
  else if (weekday==true && vacation==false) {
    return false;
  }
  else if (weekday==false && vacation==true) {
    return true;
  }
}

function monekeTrouble(asmile,bsmile) {
  if (asmile==true && bsmile==true) {
    return true;
  }
  else if (asmile==false && bsmile==false) {
    return true;
  }
  else if (asmile==false && bsmile==true)  {
    return false;
  }
  else if (asmile==true && bsmile==false) {
    return false;
  }
}
function stringTime(str,n) {
  var tme="";
  for(var i=0;i<n;i++){
  tme+=str;
}
  return tme;

}
function LuckySum(a,b,c) {
  sum=0;
  if (a==13) {
    return sum;
  }
  sum+=a;
  if (b==13) {
    return sum;
  }
  sum+=b;
  if (c==13) {
    return sum;
  }
  sum+=c;
  return sum;

}

function caught_speeding(spedd,is_birthday){
  if (is_birthday==true) {
    spedd-=5;
  }
  if (spedd<=60) {
    return 0;
  }
  else if (spedd>=61 && spedd<=80) {
    return 1;
  }
  else if(spedd>80){
    return 2;
  }
}
