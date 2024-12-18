from otree.api import *
from _static.ReCaptchaRequest import *


doc = """
Integration of reCAPTCHA v3 into oTree 5
"""


class C(BaseConstants):
    NAME_IN_URL = 'reCAPTCHA'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    gender = models.IntegerField(
        label="Are you female, male or non-binary?",
        choices=[
            [0, 'female'],
            [1, 'male'],
            [2, 'non-binary'],
        ],
        widget=widgets.RadioSelect,
        blank=False,
    )
    age = models.IntegerField(
        min=18,
        max=120,
        label="How old are you?",
        blank=False,
    )
    score_recaptcha = models.FloatField()
    valid_token = models.BooleanField()


# PAGES
class MyPage(Page):
    form_model = 'player'
    form_fields = ['gender', 'age']

    @staticmethod
    def live_method(player, data):
        # Check if the incoming data type is 'captcha'
        if data['type'] == 'captcha':
            # Call the function to validate the reCAPTCHA token, passing the token from the data
            validate = validate_recaptcha(data["response_token"])

            # Store in the player's fields
            player.score_recaptcha = validate['riskAnalysis']['score']
            player.valid_token = validate['tokenProperties']['valid']

            # Return a confirmation response to the client for this specific player
            return {player.id_in_group: True}

class redirect_bot(Page):
    template_name = '_static/redirect_bot.html'

    @staticmethod
    def is_displayed(player: Player):
        return player.score_recaptcha <= 0.3


page_sequence = [MyPage, redirect_bot]
