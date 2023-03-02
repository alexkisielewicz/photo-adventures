
$(document).ready(function () {
// Set carousel image as carousel-item's background and streches it to cover viewport
  $.each(jQuery('.carousel .carousel-item'), function (i, val) {
    $(this).css('background-image', 'url(' + $(this).find('img').attr('src') + ')').css('background-size', 'cover').find('img').css('visibility', 'hidden');
  });

  // Get current year to display in copyright
  const currentYear = new Date().getFullYear();
  $('#currentYear').text(currentYear);

  // Tooltip for heart icons in full_post template
  $('[data-toggle="tooltip-like"]').tooltip({
    placement: 'left'
  });

  
  $('.delete-post-btn').click(function (event) {
    var postId = $(this).data('post-id');
    $('#deleteForm input[name="post_id"]').val(postId);
  });



  function scrollNavbar() {
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
  }
  
  scrollNavbar();

  let animationTriggered = false;

  $(window).on('scroll', function() {
    if (!animationTriggered && $('#scrollToCounters').is(':visible')) {
      animateCounters();
      animationTriggered = true;
    }
  });
  
  function animateCounters() {
    // Counter method found in this snippet https://bootsnipp.com/snippets/5K6WW
  
    $('.count-value').each(function () {
      var finalValue = $(this).text();
      $(this).prop('Counter', 0).animate({
        Counter: finalValue
      }, {
        duration: 2000,
        easing: 'swing',
        step: function (now) {
          $(this).text(now < finalValue ? Math.ceil(now) : finalValue);
        }
      });
    });
  }

  $(window).on('scroll', function() {
    var offsetY = dociment.getElementById('#scrollToCounters').window.pageYOffset; 
    if (window.pageYOffset >= offsetY) {
      animateCounters(); 
    }
  });
  


});

// ADD STATEMENT - IF MODAL EXISTS...
const deleteConfirmationModal = new bootstrap.Modal(document.getElementById('deleteModal'))
document.querySelector('[data-target="#deleteModal"]').addEventListener('click', () => {
  deleteConfirmationModal.show()
})


// About page bootstrap accordion
const faqAccordion = new bootstrap.Accordion(document.getElementById('faqAccordion'));








