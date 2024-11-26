import requests

# Your API key, site key and project information
PROJECT_ID = "my-project-1234-12345678910"
API_KEY = "MyGoogleAPIKey123"
SITE_KEY = "MyRecaptchaSiteKey123"
ACTION = "FORM_SUBMISSION"

def validate_recaptcha(token):
    # URL for the reCAPTCHA API request
    url = f"https://recaptchaenterprise.googleapis.com/v1/projects/{PROJECT_ID}/assessments?key={API_KEY}"

    # Anfrage-Daten im JSON-Format
    request_data = {
        "event": {
            "token": token,
            "expectedAction": ACTION,
            "siteKey": SITE_KEY
        }
    }

    # Send the POST request
    response = requests.post(url, json=request_data)

    # Check the answer and return the result
    if response.status_code == 200:
        result = response.json()
        print("reCAPTCHA validation successful:", result)
        return result
    else:
        print(f"Error during reCAPTCHA validation: {response.status_code} - {response.text}")
        return None

