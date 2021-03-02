from . import models
from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Questionnaire(Page):
	form_model=models.Player
	form_fields=["WTPam","WTPri","colchoam",'recall1','recall2','Env1','Env2','Env3','Env4','Env5','Env6','Env7','Env8','Env9','EnvIdent1','EnvIdent2','EnvIdent3','Efficacy1','Efficacy2','Efficacy3','Efficacy4','Deontologist1','Deontologist2','Deontologist3','Deontologist4','Donation1','Donation2','exhaust1','risk','ambig', 'gender','age', 'language', 'uni', 'party','education','income','volun','Info','email']

	def WTPam_max(self):
		return 2

	def WTPam_min(self):
		return 0

	def WTPri_max(self):
		return 2

	def WTPri_min(self):
		return 0

	def age_min(self):
		return 18

	def before_next_page(self):
		self.player.lotchoi()
		self.player.timend()



class Results(Page):
	pass

class Auszahlung(Page):
	pass


page_sequence = [
	Questionnaire,
	Results,
	Auszahlung
]
