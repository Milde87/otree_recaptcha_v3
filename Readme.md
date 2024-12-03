# reCAPTCHA v3 for oTree 5

This is an example integration of reCAPTCHA v3 into oTree 5.11.1.
The implementation includes server-side validation of the user's response and returns a [score](https://developers.google.com/recaptcha/docs/v3?hl=de#interpreting_the_score)
 indicating the likelihood of a bot.

Starting from version v3, reCAPTCHA runs in the background, so participants are not aware of the verification process at all.

## Installation
- Install ```requests``` in your python environment.

## Setup
- Create a new [Google Cloud Project](https://console.cloud.google.com/projectcreate) (this will provide you with a ````PROJECT_ID````).
- Enable the necessary [API](https://console.cloud.google.com/apis) in this project to generate the required credentials (this will provide you with an ````API_KEY````).
- Sign up for [reCAPTCHA](https://www.google.com/recaptcha/)
  - Select the v3 Admin Console with default options.
  - Add the appropriate domains, such as ```herokuapp.com```, if you're using specific hosting providers.
  - For development purposes, also include ```localhost```.
  - This process will provide you with a ````SITE_KEY````.
- Copy ```reCAPTCHA.js``` and ```ReCaptchaRequest.py``` in your ```_static``` folder

## Usage
Add the credentials in the ```reCAPTCHA.js``` and ```ReCaptchaRequest.py```. You get them as part of the sign up process to reCAPTCHA.
```javascript
// reCAPTCHA.js
const SITE_KEY = 'MyRecaptchaSiteKey123';
```

```python
# ReCaptchaRequest.py
PROJECT_ID = "my-project-1234-12345678910"
API_KEY = "MyGoogleAPIKey123"
SITE_KEY = "MyRecaptchaSiteKey123"
ACTION = "FORM_SUBMISSION"
```
> ℹ️ **Info:** The `ACTION` parameter can represent various user interactions on your website. Here are some possible values:
> 
> - `"FORM_SUBMISSION"`: Default for submitting a form.
> - `"LOGIN"`: Used when a user attempts to log in.
> - `"SIGNUP"`: For new user registration.
> - `"COMMENT"`: When a user submits a comment or review.
> - `"SEARCH"`: When a user performs a search.
> - `"PURCHASE"`: For purchase completion or checkout process.
> - `"VIEW_PAGE"`: To track general page views.
>
> Specifying these actions helps reCAPTCHA assess bot likelihood more accurately across different interactions.



Add the necessary import statements at the top of your ``__init__.py``:
```python
# __init__.py
from otree.api import *
from _static.ReCaptchaRequest import *
```

Add a field to your player class:
```python
# __init__.py
class Player(BasePlayer):
    score_recaptcha = models.FloatField()
    valid_token = models.BooleanField()
```

On the page where you want to use reCAPTCHA, add the following function to validate the received token and save the score.
```python
# __init__.py
class MyPage(Page):
    @staticmethod
    def live_method(player, data):
        if data['type'] == 'captcha':
            validate = validate_recaptcha(data["response_token"])
            player.score_recaptcha = validate['riskAnalysis']['score']
            player.valid_token = validate['tokenProperties']['valid']
            return {player.id_in_group: True}
```

On the template for the page, add the following code:
```html
<!-- place in content block, where all formfields live -->
{{ block scripts }}
    <script src="{% static 'reCAPTCHA.js' %}"></script>
{{ endblock }}```

{{ block content }}
	<button class="otree-btn-next btn btn-primary" onclick="onSubmitForm(event)">Next</button>
{{ endblock }}

```



## Help
If you have any questions, please feel free to contact me via my [homepage](https://www.studies-services.de/en).
