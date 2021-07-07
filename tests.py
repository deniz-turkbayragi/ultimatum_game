from otree.api import Currency as c, currency_range
from . import pages
from ._builtin import Bot
from .models import Constants

import random

class PlayerBot(Bot):

    def play_round(self):

        yield (pages.IntroVideo)
        yield (pages.Offer, {'offer_player':  random.randint(0, 100)})
        yield (pages.AcceptStrategy, {'min_accepted_offer_player':  random.randint(0, 100)})


