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
