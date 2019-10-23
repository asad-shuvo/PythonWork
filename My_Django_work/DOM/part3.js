var headOne=document.querySelector('#one');
var headTwo=document.querySelector('#two');
var headThree=document.querySelector('#three');

// mouseover=Event name
headOne.addEventListener('mouseover',function () {
  headOne.textContent="Mouse Currently Over";//It will change the textContent
  headOne.style.color='red';//It will change the color of the text
})

headOne.addEventListener("mouseout",function () {
  headOne.textContent="Hover over me";
  headOne.style.color='black';
})

headTwo.addEventListener("click",function () {
  headTwo.textContent='Clicked on';
  headTwo.style.color='blue';
})
headThree.addEventListener('dblclick',function () {
  headThree.textContent='I was double clicked';
  headThree.style.color='Green';
})
