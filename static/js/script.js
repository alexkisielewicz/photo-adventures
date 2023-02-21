// set carousel image as carousel-item's background and streches it to cover viewport
$.each( jQuery('.carousel .carousel-item'), function( i, val ) {
  $(this).css('background-image','url('+$(this).find('img').attr('src')+')').css('background-size','cover').find('img').css('visibility','hidden');
});


// Tooltip for heart icons in full_post template
$(document).ready(function(){
  $('[data-toggle="tooltip-like"]').tooltip({
      placement: 'left'
    }); 
});

const body = document.body;
let lastScroll = 0;

window.addEventListener('scroll', () => {
const currentScroll = window.pageYOffset;

if (currentScroll <= 0) {
body.classList.remove('scroll-up')
}

if (currentScroll > lastScroll && !body.classList.contains('scroll-down')) {
body.classList.remove('scroll-up')
body.classList.add('scroll-down')
} 

if (currentScroll < lastScroll && body.classList.contains('scroll-down')) {
body.classList.remove('scroll-down')
body.classList.add('scroll-up')
} 

lastScroll = currentScroll;
})

$('#summernote').summernote({
  fontNames: ['Arial', 'Arial Black', 'Comic Sans MS', 'Courier New', 'Merriweather'],
  fontNamesIgnoreCheck: ['Merriweather']
});