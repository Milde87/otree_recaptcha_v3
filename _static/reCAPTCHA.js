// Define the reCAPTCHA site key
const SITE_KEY = 'MyRecaptchaSiteKey123';

// Function to dynamically load the reCAPTCHA script
(function loadReCaptcha() {
    const script = document.createElement('script');
    script.src = `https://www.google.com/recaptcha/enterprise.js?render=${SITE_KEY}`;
    script.async = true;
    script.defer = true;

    // Ensure script execution after it's loaded
    script.onload = () => {
        console.log('reCAPTCHA script loaded successfully.');

        // Initialize reCAPTCHA and prepare for execution
        grecaptcha.enterprise.ready(() => {
            grecaptcha.enterprise.execute(SITE_KEY, { action: 'FORM_SUBMISSION' }).then((token) => {
                console.log('reCAPTCHA token:', token);
                // Send the token to your backend or use it as needed
            });
        });
    };

    script.onerror = () => {
        console.error('Failed to load the reCAPTCHA script.');
    };

    // Append the script to the document head
    document.head.appendChild(script);
})();

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
