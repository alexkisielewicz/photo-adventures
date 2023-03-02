function sendMail(contactForm) {
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
            function(response) {
                // should reveive response 200 if message was sent
                if (response.status === 200) {
                    let contactFormAlert = document.getElementById("contactFormAlert");
                    contactFormAlert.classList.remove("d-none");
                    contactFormAlert.innerHTML = `Thank you! Your message was sent successfully.`;
                  }
            }, 
            // in case of an error when message is not sent 
            function(error) {
                let contactFormAlert = document.getElementById("contactFormAlert");
                contactFormAlert.classList.remove("d-none");
                contactFormAlert.classList.remove("alert-success");
                contactFormAlert.classList.add("alert-danger");
                contactFormAlert.innerHTML = `Oooops! There was a problem, your message was not sent.`;
            });

    return false;
} 