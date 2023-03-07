document.addEventListener("DOMContentLoaded", () => {

    // Selectors
    const inputTitle = document.getElementById('idTitle');
    const inputSlug = document.getElementById('id_slug');
    const inputCategory = document.getElementById('id_category');
    const inputTags = document.getElementById('id_tags');
    const inputExcerpt = document.getElementById('id_excerpt');
    // const inputImage = document.querySelector('#id_featured_image');
    const inputLocation = document.getElementById('id_location');
    
    // const radioButtons = document.querySelectorAll('input[type="radio"][name="status"]');
    const formGroup = document.getElementById('div_id_status');


    const submitButton = document.getElementById("submitButton");
    console.log(submitButton);

    inputTitle.addEventListener("input", (event) => {
        const titleValue = event.target.value;
        const slugValue = titleValue
            .trim()
            .toLowerCase()
            .replace(/[^a-z0-9]+/g, "-")
            .replace(/(^-|-$)/g, "");
        inputSlug.value = slugValue;
    });

    // set all validation status to false
    let titleIsValid, slugIsValid, categoryIsValid, tagsIsValid, excerptIsValid, locationIsValid = false;

    // I learned about regular expressions here 
    // https://html.form.guide/snippets/javascript-form-validation-using-regular-expression/ 
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

    const validateCategory = (value) => {
        if (inputCategory.value) {
            return true;
        }
        return false;
    };

    const validateTags = (value) => {
        const tagsValidation = /^([a-zA-Z]{3,}\s*,\s*)*[a-zA-Z]{3,}$/;
        if (value.match(tagsValidation) && value.length >= 4 && value.length <= 60) {
            return true;
        }
        return false;
    };

    const validateExcerpt = (value) => {
        if (value.length >= 10 && value.length <= 200) {
            return true;
        }
        return false;
    };

    const validateLocation = (value) => {
        const locationValidation = /^[a-zA-Z ,]+$/;
        if (value.match(locationValidation) && value.length >= 4 && value.length <= 40) {
            return true;
        }
        return false;
    };

    // Togle disable property on submit button, 
    // disable if any input is invalid, enable if all are valid
    const toggleSubmitButton = () => {
        if (titleIsValid && slugIsValid && categoryIsValid && tagsIsValid && excerptIsValid && locationIsValid) {
            submitButton.disabled = false;
        } else {
            submitButton.disabled = true;
        }
    };

    // Apply bootstrap style
    const addInvalidStyle = (el) => {
        el.classList.remove("is-valid");
        el.classList.add("is-invalid");
    };

    // Apply bootstrap style
    const addValidStyle = (el) => {
        el.classList.remove("is-invalid");
        el.classList.add("is-valid");
    };

    const disableSubmitButton = () => {
        submitButton.disabled = true;
        submitButton.classList.add("submit-disabled-state");
    };

    const enableSubmitButton = () => {
        submitButton.disabled = false;
        submitButton.classList.remove("submit-disabled-state");
    };

    const updateSubmitButton = () => {
        if (titleIsValid && slugIsValid && categoryIsValid && tagsIsValid && excerptIsValid && locationIsValid) {
            enableSubmitButton();
        } else {
            disableSubmitButton();
        }
    };

    // Event listeners
    inputTitle.addEventListener("input", (event) => {
        const titleValue = event.target.value;
        if (validateTitle(titleValue)) {
            titleIsValid = true;
            addValidStyle(inputTitle);
        } else {
            titleIsValid = false;
            addInvalidStyle(inputTitle);
        }
        updateSubmitButton();
    });

    inputSlug.addEventListener("input", (event) => {
        const slugValue = event.target.value;
        if (validateSlug(slugValue)) {
            slugIsValid = true;
            addValidStyle(inputSlug);
        } else {
            slugIsValid = false;
            addInvalidStyle(inputSlug);
        }
        updateSubmitButton();
    });

    inputCategory.addEventListener("input", (event) => {
        const categoryValue = event.target.value;
        if (validateCategory(categoryValue)) {
            categoryIsValid = true;
            addValidStyle(inputCategory);
        } else {
            categoryIsValid = false;
            addInvalidStyle(inputCategory);
        }
        updateSubmitButton();
    });

    inputTags.addEventListener("input", (event) => {
        const tagsValue = event.target.value;
        if (validateTags(tagsValue)) {
            tagsIsValid = true;
            addValidStyle(inputTags);
        } else {
            tagsIsValid = false;
            addInvalidStyle(inputTags);
        }
        updateSubmitButton();
    });

    inputExcerpt.addEventListener("input", (event) => {
        const excerptValue = event.target.value;
        if (validateExcerpt(excerptValue)) {
            excerptIsValid = true;
            addValidStyle(inputExcerpt);
        } else {
            excerptIsValid = false;
            addInvalidStyle(inputExcerpt);
        }
        updateSubmitButton();
    });

    inputLocation.addEventListener("input", (event) => {
        const locationValue = event.target.value;
        if (validateLocation(locationValue)) {
            locationIsValid = true;
            addValidStyle(inputLocation);
        } else {
            locationIsValid = false;
            addInvalidStyle(inputLocation);
        }
        updateSubmitButton();
    });

    // Call the function
    updateSubmitButton();
});