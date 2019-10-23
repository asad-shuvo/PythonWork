$('h1').click(function () {
  console.log('There was a click');
  $(this).text("I was chaned");
})


$('li').click(function() {
  console.log('Any li was clicked');
})


// Key press
// $('input').eq(0).keypress(function(){
//   $('h3').toggleClass('turnBlue');
// })

$('input').eq(0).keypress(function(event){
  if(event.which===13)///13=Enter
  $('h3').toggleClass('turnBlue');
})

$('h1').on('mouseenter',function () {
  $(this).toggleClass('turnRed');
})

// Animation
// $('input').eq(1).on('click',function() {
//   $('.container').fadeOut(3000);
// })
$('input').eq(1).on('click',function() {
  $('.container').slideUp(3000);
})
