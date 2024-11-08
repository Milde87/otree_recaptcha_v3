import requests

# Your API key, site key and project information
PROJECT_ID = "my-project-8441-1730816628883"
API_KEY = "AIzaSyAu10qjH2zsgswm-8_MCki6taRgm46m_n4"
SITE_KEY = "6Ld3CXYqAAAAAL5_L_TNmFjLP1TVzw9XDpBxFJJr"
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
        print("reCAPTCHA-Validierung erfolgreich:", result)
        return result['riskAnalysis']['score']
    else:
        print(f"Fehler bei der reCAPTCHA-Validierung: {response.status_code} - {response.text}")
        return None

