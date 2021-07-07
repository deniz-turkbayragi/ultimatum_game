from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
import random
from datetime import timedelta, datetime

doc = """
Ultimatum game with two treatments: direct response and strategy method.
In the former, one player makes an offer and the other either accepts or rejects.
It comes in two flavors, with and without hypothetical questions about the second player's response to offers other than the one that is made.
In the latter treatment, the second player is given a list of all possible offers, and is asked which ones to accept or reject.
"""


class Constants(BaseConstants):
    name_in_url = 'ultimatum'
    players_per_group = None
    num_rounds = 1
    roles = ['proposer', 'responder']
    instructions_template = 'ultimatum/instructions.html'

    endowment = 200
    payoff_if_rejected = 0


class Subsession(BaseSubsession):
    pass
    # def creating_session(self):
    #     self.group_randomly()


class Group(BaseGroup):

    offer = models.CurrencyField()
    min_accepted_offer = models.IntegerField()
    offer_accepted = models.BooleanField()

    def set_roles(self):

        p1 = self.get_player_by_id(1)
        p2 = self.get_player_by_id(2)

        self.offer = p1.offer_player
        self.min_accepted_offer = p2.min_accepted_offer_player

    def set_payoffs(self):

        p1 = self.get_player_by_id(1)
        p2 = self.get_player_by_id(2)

        if self.offer >= self.min_accepted_offer:
            self.offer_accepted = True
            p1.payoff_ultimatum = Constants.endowment - self.offer
            p2.payoff_ultimatum = self.offer

        else:
            self.offer_accepted = False
            p1.payoff_ultimatum = 0
            p2.payoff_ultimatum = 0

        print('Player 1\'s offer:', self.offer)
        print('Player 2\'s min accepted offer:', self.min_accepted_offer)
        print('Is offer accepted:', self.offer_accepted)

        print('Player 1\'s payoff in ultimatum game:', p1.payoff_ultimatum)
        print('Player 2\'s payoff in ultimatum game:', p2.payoff_ultimatum)


        for p in self.get_players():
            p.participant.vars['payoff_ultimatum'] = p.payoff_ultimatum
            print('Payoff Ultimatum (participant var):', p.participant.vars['payoff_ultimatum'])


class Player(BasePlayer):

    offer_player = models.IntegerField(min=0, max=Constants.endowment, label="")
    min_accepted_offer_player = models.IntegerField(min=0, max=Constants.endowment, label="")
    role = models.StringField()
    payoff_ultimatum = models.IntegerField()

    def role(self):
        if self.id_in_group == 1:
            return 'Proposer'
        if self.id_in_group == 2:
            return 'Responder'
