from otree.api import (
	models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
	Currency as c, currency_range
)


author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
	name_in_url = 'donation'
	players_per_group = None
	num_rounds = 1


class Subsession(BaseSubsession):
	pass


class Group(BaseGroup):
	pass


class Player(BasePlayer):
	spendeWWF= models.FloatField(blank=True)
	spendeMeerPlastik= models.FloatField(blank=True)
	spendeMannTafel= models.FloatField(blank=True)
	totaldon=models.FloatField(initial=0)
	def calc_payoff(self):
		if self.spendeWWF==None:
			self.spendeWWF=0
		else:
			self.totaldon+=self.spendeWWF
		if self.spendeMeerPlastik==None:
			self.spendeMeerPlastik=0
		else:
			self.totaldon+=self.spendeMeerPlastik
		if self.spendeMannTafel==None:
			self.spendeMannTafel=0
		else:
			self.totaldon+=self.spendeMannTafel
		self.participant.vars['doni']=self.totaldon











#------------Questionnaire------------------------------------------
	



	

