// set carousel image as carousel-item's background and streches it to cover viewport
$(document).ready(function () {

  $.each(jQuery('.carousel .carousel-item'), function (i, val) {
    $(this).css('background-image', 'url(' + $(this).find('img').attr('src') + ')').css('background-size', 'cover').find('img').css('visibility', 'hidden');
  });

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
  
});

// ADD STATEMENT - IF MODAL EXISTS...
const deleteConfirmationModal = new bootstrap.Modal(document.getElementById('deleteModal'))
document.querySelector('[data-target="#deleteModal"]').addEventListener('click', () => {
  deleteConfirmationModal.show()
})


// About page bootstrap accordion
const faqAccordion = new bootstrap.Accordion(document.getElementById('faqAccordion'));