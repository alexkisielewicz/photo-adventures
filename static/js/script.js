$(document).ready(function () {
  // Get current year to display in copyright
  const currentYear = new Date().getFullYear();
  $('#currentYear').text(currentYear);

  // Tooltip for heart icons in full_post template
  $('[data-toggle="tooltip-like"]').tooltip({
    placement: 'left'
  });


// Function used for hiding navbar on scroll down and showing it back on scroll up.
function scrollNavbar() {
  const body = document.body;
  let lastScroll = 0;

  $(window).on('scroll', () => {
    const currentScroll = $(window).scrollTop();

    if (currentScroll <= 0) {
      body.classList.remove('scroll-up');
    }

    if (currentScroll > lastScroll && !body.classList.contains('scroll-down')) {
      body.classList.remove('scroll-up');
      body.classList.add('scroll-down');
    }

    if (currentScroll < lastScroll && body.classList.contains('scroll-down')) {
      body.classList.remove('scroll-down');
      body.classList.add('scroll-up');
    }

    lastScroll = currentScroll;
  });
}

scrollNavbar();

let animationTriggered = false;

function animateCounters() {
  // Method to animate counters found in this snippet https://bootsnipp.com/snippets/5K6WW

  $('.count-value').each(function () {
    var finalValue = $(this).text();
    $(this).prop('Counter', 0).animate({
      Counter: finalValue
    }, {
      duration: 1200,
      easing: 'swing',
      step: function (now) {
        $(this).text(now < finalValue ? Math.ceil(now) : finalValue);
      }
    });
  });
}

$(window).on('scroll', function () {
  let offsetY = $('#scrollToCounters').offset().top;
  if (window.pageYOffset >= offsetY && !animationTriggered) {
    animateCounters();
    animationTriggered = true;
  }
});

/* User dashboard
Hide Divs and Headers if there's no dynamic django content inside them */
if ($('#draftsHeader').text().includes('(0):')) {
  $('#draftsContainer').hide();
}

if ($('#awaitingHeader').text().includes('(0):')) {
  $('#awaitingContainer').hide();
}

if ($('#publishedHeader').text().includes('(0):')) {
  $('#publishedContainer').hide();
}

// Select the toast element to display django messages
const toastEl = document.querySelector('.toast')

// Create a new Bootstrap toast instance
let toast = new bootstrap.Toast(toastEl)

// Call the show method to display the toast
toast.show()


});

// About page - initialize bootstrap accordion. 
if (document.getElementById('faqAccordion')) {
  let accordion = document.getElementById('faqAccordion');
  let myAccordion = new bootstrap.Collapse(accordion);
}