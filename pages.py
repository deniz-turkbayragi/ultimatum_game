from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class FirstWaitPage(WaitPage):
    pass
    #group_by_arrival_time = True

class IntroVideo(Page):

    timeout_seconds = 150

    def vars_for_template(self):
        return {"image_path": "global/background_ultimatum.jpg",
                'audio_path': 'global/ultimatum.mp3'}


class Introduction(Page):
    pass


class Offer(Page):

    timeout_seconds = 150

    form_model = 'player'
    form_fields = ['offer_player']


class AcceptStrategy(Page):

    timeout_seconds = 150

    form_model = 'player'
    form_fields = ['min_accepted_offer_player']


class ResultsWaitPage(WaitPage):
    pass

    # def after_all_players_arrive(self):
    #     self.group.set_roles()
    #     self.group.set_payoffs()


class Results(Page):
    pass


page_sequence = [IntroVideo,
                 Offer,
                 AcceptStrategy,
                 ]
