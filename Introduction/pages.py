from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from . import models
from .models import Constants
import time



class Intro(Page):
	def before_next_page(self):
		self.player.tttime()

class Info(Page):
	def before_next_page(self):
		self.player.ttime()

class Anleitung(Page):
	def before_next_page(self):
		self.player.time()




page_sequence = [
	Intro,
	Info,
    Anleitung
]
