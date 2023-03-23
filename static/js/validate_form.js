document.addEventListener("DOMContentLoaded", () => {
    /* 
    I learned about regular expressions on this website and selected different
    sets of allowed characters for each validating input.
    https://html.form.guide/snippets/javascript-form-validation-using-regular-expression/ 
    */
    
    /* Define 7 form input fields and form submit button,
    validaiotn of uploaded image file was marked as feature for potential future enhancement */
    const inputTitle = document.getElementById('idTitle');
    const inputSlug = document.getElementById('id_slug');
    const inputCategory = document.getElementById('id_category');
    const inputTags = document.getElementById('id_tags');
    const inputExcerpt = document.getElementById('id_excerpt');
    const inputLocation = document.getElementById('id_location');
    const radioButtons = document.querySelectorAll('input[type="radio"][name="status"]');
    const submitButton = document.getElementById("submitButton");

    // Process title input value to prefill slug input as words separated with dash
    inputTitle.addEventListener("input", (event) => {
        const titleValue = event.target.value;
        const slugValue = titleValue
            .trim()
            .toLowerCase()
            .replace(/[^a-z0-9]+/g, "-")
            .replace(/(^-|-$)/g, "");
        inputSlug.value = slugValue;
    });

    // Initially set all 7 validation inputs values to false in order to disable submit button by default
    let isValid = {
        title: false,
        slug: false,
        category: false,
        tags: false,
        excerpt: false,
        location: false,
        status: false,
      };
    
    // Validate each of 7 input field against allowed regular expression
    const validateTitle = (value) => {
        const titleValidation = /^[a-zA-Z0-9 ,]+$/;
        if (value.match(titleValidation) && value.length >= 5 && value.length <= 50) {
            return true;
        }
        return false;
    };

    const validateSlug = (value) => {
        const slugValidation = /^[a-z0-9]+(?:-[a-z0-9]+)*$/;
        if (value.match(slugValidation) && value.length >= 5 && value.length <= 50) {
            return true;
        }
        return false;
    };

    // Validate select input, one has to be selected
    const validateCategory = (value) => {
        if (inputCategory.value) {
            return true;
        }
        return false;
    };

    /* Allowed minimal tag length is 3 characters, coma separated words
    Shortest input should be 1 tag, max 60 characters */
    const validateTags = (value) => {
        const tagsValidation = /^([a-zA-Z]{3,}\s*,\s*)*[a-zA-Z]{3,}$/;
        if (value.match(tagsValidation) && value.length >= 3 && value.length <= 60) {
            return true;
        }
        return false;
    };

    // Allowed length range for excerpt is 10-200 characters
    const validateExcerpt = (value) => {
        if (value.length >= 10 && value.length <= 200) {
            return true;
        }
        return false;
    };

    // Allowed aplha characters and coma, length range 4-40 characters
    const validateLocation = (value) => {
        const locationValidation = /^[a-zA-Z ,]+$/;
        if (value.match(locationValidation) && value.length >= 4 && value.length <= 40) {
            return true;
        }
        return false;
    };

    // Add event listeners to each radio buttons
    radioButtons.forEach(function (radioButton) {
        radioButton.addEventListener('click', function () {
            // Remove is-valid class from all radio buttons
            radioButtons.forEach(function (radioButton) {
                radioButton.classList.remove('is-valid');
            });
    
            if (this.checked) {
                // Apply is-valid bootstrap class to clicked radio button
                this.classList.add('is-valid');
                isValid.status = true;
            } else {
                // Apply is-invalid bootstrap class to clicked radio button
                this.classList.remove('is-valid');
                isValid.status = false;
            }
            updateSubmitButton();
        });
    });

    /* Togle disable property on submit button, 
    disable if any input is invalid, enable if all are valid */
    const toggleSubmitButton = () => {
        const isValidDict = Object.values(isValid);
        if (isValidDict.every(value => value === true)) {
          submitButton.disabled = false;
        } else {
          submitButton.disabled = true;
        }
      };

    // Apply bootstrap style for valid input
    const addInvalidStyle = (el) => {
        el.classList.remove("is-valid");
        el.classList.add("is-invalid");
    };

    // Apply bootstrap style for invalid input
    const addValidStyle = (el) => {
        el.classList.remove("is-invalid");
        el.classList.add("is-valid");
    };

    // Set disable property for form submit button = not clickable
    const disableSubmitButton = () => {
        console.log(submitButton);
        submitButton.disabled = true;
        submitButton.classList.add("submit-disabled-state");
    };

    // Remove disable property for form submit button = clickable
    const enableSubmitButton = () => {
        submitButton.disabled = false;
        submitButton.classList.remove("submit-disabled-state");
    };

    // Check if dictionary isValid has all input key values equals to True
    const updateSubmitButton = () => {
        const isValidDict = Object.values(isValid);
        if (isValidDict.every(value => value === true)) {
            // Allow to proceed with form submition
            enableSubmitButton();
        } else {
            // Don't allow to submit the form
            disableSubmitButton();
        }
    };

    // Event listeners for all input fields that are being validated
    inputTitle.addEventListener("input", (event) => {
        const titleValue = event.target.value;
        if (validateTitle(titleValue)) {
            isValid.title = true;
            addValidStyle(inputTitle);
        } else {
            isValid.title = false;
            addInvalidStyle(inputTitle);
        }
        updateSubmitButton();
    });

    inputSlug.addEventListener("input", (event) => {
        const slugValue = event.target.value;
        if (validateSlug(slugValue)) {
            isValid.slug = true;
            addValidStyle(inputSlug);
        } else {
            isValid.slug = false;
            addInvalidStyle(inputSlug);
        }
        updateSubmitButton();
    });

    inputCategory.addEventListener("input", (event) => {
        const categoryValue = event.target.value;
        if (validateCategory(categoryValue)) {
            isValid.category = true;
            addValidStyle(inputCategory);
        } else {
            isValid.category = false;
            addInvalidStyle(inputCategory);
        }
        updateSubmitButton();
    });

    inputTags.addEventListener("input", (event) => {
        const tagsValue = event.target.value;
        if (validateTags(tagsValue)) {
            isValid.tags = true;
            addValidStyle(inputTags);
        } else {
            isValid.tags = false;
            addInvalidStyle(inputTags);
        }
        updateSubmitButton();
    });

    inputExcerpt.addEventListener("input", (event) => {
        const excerptValue = event.target.value;
        if (validateExcerpt(excerptValue)) {
            isValid.excerpt = true;
            addValidStyle(inputExcerpt);
        } else {
            isValid.excerpt = false;
            addInvalidStyle(inputExcerpt);
        }
        updateSubmitButton();
    });

    inputLocation.addEventListener("input", (event) => {
        const locationValue = event.target.value;
        if (validateLocation(locationValue)) {
            isValid.location = true;
            addValidStyle(inputLocation);
        } else {
            isValid.location = false;
            addInvalidStyle(inputLocation);
        }
        updateSubmitButton();
    });

    // Call the function that checks if all validations are set to True
    updateSubmitButton();
});