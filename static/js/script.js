$(document).ready(function () {
    // Get current year to display in copyright
    const currentYear = new Date().getFullYear();
    $('#currentYear').text(currentYear);

    // Tooltip for heart icons in full_post template
    $('[data-toggle="tooltip-like"]').tooltip({
        placement: 'left'
    });

    // Method to animate counters found in this snippet https://bootsnipp.com/snippets/5K6WW
    let animationTriggered = false;

    function animateCounters() {
        // Function animates digits in html containers 
        $('.count-value').each(function () {
            var finalValue = $(this).text();
            // Idea for animation block of code found here https://bootsnipp.com/snippets/5K6WW
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

    // Animation function executes on scroll when containers reach bottom of the window
    // Trigger position is callculated from top of the window - windows height + 100px 
    $(window).on('scroll', function () {
        let windowHeight = window.innerHeight;
        let offsetY = $('#scrollToCounters').offset().top - windowHeight + 100;
        if (window.pageYOffset >= offsetY && !animationTriggered) {
            animateCounters();
            animationTriggered = true;
        }
    });


    submitButton = document.querySelector('button[type=submit]');
    submitButton.setAttribute('disabled', true);

    document.getElementById("contactForm").addEventListener("submit", function (event) {
        let recaptcha = grecaptcha.getResponse();
        if (recaptcha.length === 0) {
            event.preventDefault();
            alert("Please validate the reCAPTCHA.");
            let contactFormAlert = document.getElementById("contactFormAlert");
            contactFormAlert.classList.remove("d-none");
            contactFormAlert.classList.remove("alert-success");
            contactFormAlert.classList.add("alert-danger");
            contactFormAlert.innerHTML = `Please validate the reCAPTCHA before submit.`;
        } else {
            submitButton.removeAttribute('disabled');
        }
    });

});

function hideEmptySections() {
    /* User dashboard function
    Hides Divs and Headers if there's no dynamic django content inside them */
    if ($('#draftsHeader').text().includes('(0):')) {
        $('#draftsContainer').hide();
    }

    if ($('#awaitingHeader').text().includes('(0):')) {
        $('#awaitingContainer').hide();
    }

    if ($('#publishedHeader').text().includes('(0):')) {
        $('#publishedContainer').hide();
    }
}

hideEmptySections()