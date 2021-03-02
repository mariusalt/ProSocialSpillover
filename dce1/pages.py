from . import models
from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class dceques(Page):
	form_model=models.Player
	form_fields=["submitted_answer",'sec']

	def vars_for_template(self):
		return self.player.vars_for_template()
		

page_sequence = [
	dceques
]
