// Define the reCAPTCHA site key
const SITE_KEY = '6Ld3CXYqAAAAAL5_L_TNmFjLP1TVzw9XDpBxFJJr';

// Event handler for form submission
function onSubmitForm(event) {
    event.preventDefault(); // Prevents the form from being sent automatically

    // Initialize reCAPTCHA and request a token
    grecaptcha.enterprise.ready(async () => {
        // Generate a reCAPTCHA token for the specified action
        const token = await grecaptcha.enterprise.execute(SITE_KEY, {action: 'FORM_SUBMISSION'});

        // Send the token to the server (e.g., for validation)
        liveSend(
            {
                'type': 'captcha',
                'response_token': token
            }
        )
    });
}

// Server response handler
function liveRecv(data) {
    // Submit the form after receiving server confirmation
    document.getElementById("form").submit();
}
