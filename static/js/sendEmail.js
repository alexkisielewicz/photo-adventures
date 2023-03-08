function sendMail(contactForm) {

    let contactFormAlert = document.getElementById("contactFormAlert");

    // Display the error text if the user didn't solve the captcha
    let userResponse = grecaptcha.getResponse();
    if (userResponse.length === 0) {
        contactFormAlert.classList.remove("d-none");
        contactFormAlert.classList.add("alert-danger");
        contactFormAlert.innerHTML = `Please complete the captcha before submition.`;
        return false;
    }
    }

    let templateParams = {
        "from_name": contactForm.fullname.value,
        "from_email": contactForm.emailaddress.value,
        "message": contactForm.messagebody.value
    };

    const service = "service_012g84a"
    const publicKey = "g1axgIaSxxc6CzUiB";
    const template = "django_contact"

    emailjs.init(service);
    emailjs.send(service, template, templateParams, publicKey)
        .then(
            function (response) {
                // Should reveive response 200 if message was sent
                if (response.status === 200) {
                    contactFormAlert.classList.remove("d-none"); 
                    contactFormAlert.classList.remove("alert-danger");
                    contactFormAlert.classList.add("alert-success")
                    contactFormAlert.innerHTML = `Thank you! Your message was sent successfully.`;
                }
            },
            // In case of an error when message is not sent 
            function (error) {
                contactFormAlert.classList.remove("d-none");
                contactFormAlert.classList.add("alert-danger");
                contactFormAlert.innerHTML = `Oooops! There was a problem, your message was not sent.`;
            });

    return false;
}