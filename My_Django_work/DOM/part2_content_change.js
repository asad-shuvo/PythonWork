var p=document.querySelector('p');
p.textContent="NEW content";

p.innerHTML="<strong>I'm bold</strong>";
var special=document.querySelector('#special');
var specialA=special.querySelector('a');
specialA.getAttribute('href');
specialA.setAttribute('href','https://www.amazon.com');
