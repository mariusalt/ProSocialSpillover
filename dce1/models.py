from otree.api import (
	models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
	Currency as c, currency_range
)
import random
import csv
import pandas as pd

author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
	name_in_url = 'dce1'
	num_rounds = 6
	players_per_group = None
	
#	if random.choice([1,2])==1:
#		df1 = pd.read_csv('dce1/alt1lte1.csv', delimiter=',')
#		sets1 = [list(x) for x in df1.values]
#		df2 = pd.read_csv('dce1/alt2lte1.csv', delimiter=',')
#		sets2 = [list(x) for x in df2.values]
#	else:
#		df1 = pd.read_csv('dce1/alt3lte1.csv', delimiter=',')
#		sets1 = [list(x) for x in df1.values]
#		df2 = pd.read_csv('dce1/alt4lte1.csv', delimiter=',')
#		sets2 = [list(x) for x in df2.values]
#
#	dfl1 = pd.read_csv('dce1/alt1large.csv', delimiter=',')
#	setsl1 = [list(x) for x in dfl1.values]
#	dfl2 = pd.read_csv('dce1/alt2large.csv', delimiter=',')
#	setsl2 = [list(x) for x in dfl2.values]


	


class Subsession(BaseSubsession):
	def creating_sessions(self):
		if random.choice([1,2])==1:
			df1 = pd.read_csv('dce1/alt1lte2.csv', delimiter=',')
			sets1 = [list(x) for x in df1.values]
			df2 = pd.read_csv('dce1/alt2lte2.csv', delimiter=',')
			sets2 = [list(x) for x in df2.values]
		else:
			df1 = pd.read_csv('dce1/alt3lte2.csv', delimiter=',')
			sets1 = [list(x) for x in df1.values]
			df2 = pd.read_csv('dce1/alt4lte2.csv', delimiter=',')
			sets2 = [list(x) for x in df2.values]

		dfl1 = pd.read_csv('dce1/alt1large.csv', delimiter=',')
		setsl1 = [list(x) for x in dfl1.values]
		dfl2 = pd.read_csv('dce1/alt2large.csv', delimiter=',')
		setsl2 = [list(x) for x in dfl2.values]
		for p in self.get_players():
			if p.participant.vars['choi']==12:
				self.session.vars['questions1']=sets1
				self.session.vars['questions2']=sets2
			else:
				self.session.vars['questions1']=setsl1
				self.session.vars['questions2']=setsl2
		
			set_data1 = p.current_set1()
			p.set_attr11 = str(set_data1[1])
			p.set_attr12 = str(set_data1[2])
			p.set_attr13 = str(set_data1[3])
			p.set_attr14 = str(set_data1[4])
			p.set_attr16 = random.choice(["Inland","Ausland"])
			if p.participant.vars['dcet']=="base":
				p.set_attr17 = str(set_data1[5])
			else:
				p.set_attr17 = str(set_data1[6])


			set_data2 = p.current_set2()
			p.set_attr21 = str(set_data2[1])
			p.set_attr22 = str(set_data2[2])
			p.set_attr23 = str(set_data2[3])
			p.set_attr24 = str(set_data2[4])
			p.set_attr26 = p.set_attr16 
			if p.participant.vars['dcet']=="base":
				p.set_attr27 = str(set_data2[5])
			else:
				p.set_attr27 = str(set_data2[6])
			






class Group(BaseGroup):
	pass


class Player(BasePlayer):
	set_id1 = models.PositiveIntegerField()
	set_attr11 = models.StringField()
	set_attr12 = models.StringField()
	set_attr13 = models.StringField()
	set_attr14 = models.StringField()
	set_attr16 = models.StringField()
	set_attr17 = models.StringField()

	set_id2 = models.PositiveIntegerField()
	set_attr21 = models.StringField()
	set_attr22 = models.StringField()
	set_attr23 = models.StringField()
	set_attr24 = models.StringField()
	set_attr26 = models.StringField()
	set_attr27 = models.StringField()

	sec = models.IntegerField()


	submitted_answer = models.IntegerField(
		choices=[1, 2, 3],
		widget=widgets.RadioSelect())

 #   correct_answers=models.IntegerField(
  #  	default=0
   # 	)

	def current_set1(self):
		return self.session.vars['questions1'][(self.round_number-1)]

	def current_set2(self):
		return self.session.vars['questions2'][(self.round_number-1)]

	def current_set3(self):
		return self.session.vars['questions'][(self.round_number-1)*5 + 2]

	def current_set4(self):
		return self.session.vars['questions'][(self.round_number-1)*5 + 3]



	def vars_for_template(self):
		return {
		'attr11': self.set_attr11,
		'attr12': self.set_attr12,
		'attr13': self.set_attr13,
		'attr14': self.set_attr14,
		'attr16': self.set_attr16,
		'attr17': self.set_attr17,
		'attr21': self.set_attr21,
		'attr22': self.set_attr22,
		'attr23': self.set_attr23,
		'attr24': self.set_attr24,
		'attr26': self.set_attr26,
		'attr27': self.set_attr27,
		}



#    def count(self):
 #   	if self.submitted_answer == self.solution:
  #  		self.correct_answers=self.correct_answers.in_previous_rounds() + 1


