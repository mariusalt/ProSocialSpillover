from otree.api import (
	models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
	Currency as c, currency_range
)
from django import forms
import time



author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
	name_in_url = 'dce'
	players_per_group = None
	num_rounds = 1
	


class Subsession(BaseSubsession):
	pass


class Group(BaseGroup):
	pass


class Player(BasePlayer):
	test_attempts = models.IntegerField(blank=True, initial=1)
	time2 = models.FloatField()
	time21 = models.FloatField()
	time22 = models.FloatField()
	time3 = models.FloatField()
	time31 = models.FloatField()
	time32 = models.FloatField()
	time4 = models.FloatField()
	time41 = models.FloatField()
	time42 = models.FloatField()
	time5 = models.FloatField()
	time51 = models.FloatField()
	time52 = models.FloatField()
	time6 = models.FloatField()
	time61 = models.FloatField()
	time62 = models.FloatField()
	time7 = models.FloatField()
	timein21 = models.FloatField()
	timein22 = models.FloatField()
	timein31 = models.FloatField()
	timein32 = models.FloatField()
	timein41 = models.FloatField()
	timein42 = models.FloatField()
	timein51 = models.FloatField()
	timein52 = models.FloatField()
	timein61 = models.FloatField()
	timein62 = models.FloatField()


	def time(self):
		self.time2=time.time()
	def tim3(self):
		self.time3=time.time()
	def tim4(self):
		self.time4=time.time()
	def tim5(self):
		self.time5=time.time()
	def tim6(self):
		self.time6=time.time()
	def tim7(self):
		self.time7=time.time()
	def tim21(self):
		self.time21=time.time()
	def tim31(self):
		self.time31=time.time()
	def tim41(self):
		self.time41=time.time()
	def tim51(self):
		self.time51=time.time()
	def tim61(self):
		self.time61=time.time()
	def tim22(self):
		self.time22=time.time()
	def tim32(self):
		self.time32=time.time()
	def tim42(self):
		self.time42=time.time()
	def tim52(self):
		self.time52=time.time()
	def tim62(self):
		self.time62=time.time()
	def timin21(self):
		self.timein21=time.time()
	def timin31(self):
		self.timein31=time.time()
	def timin41(self):
		self.timein41=time.time()
	def timin51(self):
		self.timein51=time.time()
	def timin61(self):
		self.timein61=time.time()
	def timin22(self):
		self.timein22=time.time()
	def timin32(self):
		self.timein32=time.time()
	def timin42(self):
		self.timein42=time.time()
	def timin52(self):
		self.timein52=time.time()
	def timin62(self):
		self.timein62=time.time()

	FE6 = models.StringField(
    blank=True,
    label="",
    widget=forms.CheckboxSelectMultiple(
        choices=[
            [1, 'Gibt die Prozessorleistung an.'],
            [2, 'Gibt die Downloadgeschwindigkeit gemessen in Milli-Ampere-Stunden an.'],
            [3, 'Fungiert als Richtwert für das Ladekabel.'],
            [4, 'Gibt an, wie viel Stunden Strom ein Akku bei einer Entladungsspannung von 1 mA liefert.'],
        ],
    )
)

	
	wrong_Q1_1 = models.IntegerField(initial=0)

	Q1_2 = models.StringField(
    blank=True,
    label="",
    widget=forms.CheckboxSelectMultiple(
        choices=[
            [1, 'HD hat eine bessere Auflösung als 4K.'],
            [2, '4K-Kameratechnologie hat mindestens eine Auflösung von 4096x2160 Pixel.'],
            [3, 'SD hat die geringste Anzahl an Pixel pro Bild.']
        ],
    )
)

	wrong_Q1_2 = models.IntegerField(initial=0)

	Q1_3 = models.IntegerField(
		blank=True, 
		verbose_name="fdnm,t Ihr Studienfach?")

	wrong_Q1_3 = models.IntegerField(initial=0)

	Q1_4 = models.IntegerField(
		blank=True, 
		verbose_name="Falls Sie oder studiert haben, was ist Ihr Studienfach?")

	wrong_Q1_4 = models.IntegerField(initial=0)

	Q1_5 = models.IntegerField(
		blank=True, 
		verbose_name="Falls Sie oder studiert haben, was ist Ihr Studienfach?")

	wrong_Q1_5 = models.IntegerField(initial=0)

	wrong = models.IntegerField(initial=0)

	def error1(self):
		self.wrong_Q1_1 +=1
		self.wrong+=1
		#
	def error11(self):
		self.wrong_Q1_1 +=1
		self.wrong+=1
		self.test_attempts+=1

	def error2(self):
		self.wrong_Q1_2 +=1
		self.wrong+=1
		#
	def error21(self):
		self.wrong_Q1_2 +=1
		self.wrong+=1
		self.test_attempts+=1



