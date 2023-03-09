// Function check if captcha is solved. 
// It is solved if response from API is longer than 0.
function checkCaptcha(event) {
    event.preventDefault();
    let captchaAlert = document.getElementById("captchaAlert");
    let userResponse = grecaptcha.getResponse();
    // Check for reCaptcha API response
    if (userResponse.length === 0) {
      captchaAlert.classList.remove("d-none");
      captchaAlert.classList.add("alert-danger");
      captchaAlert.innerHTML = `Please solve the captcha before submission.`;
      return false;
    } else {
      // Submit the form if captcha is solved
      event.target.submit();
    }
  }