from otree.api import (
	models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
	Currency as c, currency_range
)
import random
import time


author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
	name_in_url = 'Introduction'
	players_per_group = None
	num_rounds = 1



class Subsession(BaseSubsession):
	def creating_session(self):
		players = self.get_players()
		for p in players:
			t=random.choice([0,1,2,3,5])
			if t==0:
				p.treatment='noenvi'
				p.participant.vars['type']='noenvi'

			elif t==1:
				p.treatment='baseline'
				p.participant.vars['type']='baseline'
			elif t==2:
				p.treatment='nudge'
				p.participant.vars['type']='nudge'
			elif t==3:
				p.treatment='lowmon'
				p.participant.vars['type']='lowmon'
			elif t==5:
				p.treatment='force'
				p.participant.vars['type']='force'


			b=random.choice([0,1,2])
			if b==0:
				p.participant.vars['dcet']='base'
				p.dcetreat='base'
			elif b==1:
				p.participant.vars['dcet']='amb'
				p.dcetreat='amb'
			else:
				p.participant.vars['dcet']='cheat'
				p.dcetreat='cheat'
			
			r=0#random.choice([0,1])
			if r==0:
				p.numcho=12
				p.participant.vars['choi']=12
			else:
				p.numcho=24
				p.participant.vars['choi']=24
			


class Group(BaseGroup):
	pass


class Player(BasePlayer):
	dcetreat=models.StringField()
	treatment = models.StringField(
		)
	numcho=models.IntegerField()
	time=models.FloatField()
	time0=models.FloatField()
	time1=models.FloatField()

	def tttime(self):
		self.time0=time.time()

	def ttime(self):
		self.time0=time.time()

	def time(self):
		self.time1=time.time()
	

	def define_plus(self):
		if self.treatment=='highmon':
			self.participant.vars['endowment']=12
		elif self.treatment=='lowmon':
			self.participant.vars['endowment']=7
		else:
			self.participant.vars['endowment']=12

#	def treatments(self):
#		if self.treatment=='baseline':
#			self.participant.vars['type']='baseline'
#		elif self.treatment=='nudge':
#			self.participant.vars['type']='nudge'
#		elif self.treatment=='lowmon':
#			self.participant.vars['type']='lowmon'
#		elif self.treatment=='highmon':
#			self.participant.vars['type']='highmon'
#		else:
#			self.participant.vars['type']='force'

######only for preparation purposes


		