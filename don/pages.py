from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants


class MyPage(Page):
	form_model=models.Player
	form_fields=["spendeWWF","spendeMeerPlastik","spendeMannTafel"]

	def error_message(self, values):
		try:
			if values["spendeWWF"] + values["spendeMeerPlastik"] + values["spendeMannTafel"] > 12:
				 	return 'Sie können maximal ihren gesamten auszuzahlenden Betrag spenden'
		except TypeError:
			try:
				if values["spendeMeerPlastik"] + values["spendeMannTafel"] > 12:
				 	return 'Sie können maximal ihren gesamten auszuzahlenden Betrag spenden'
			except TypeError:
				try:
					if values["spendeWWF"] + values["spendeMeerPlastik"] > 12:
						return 'Sie können maximal ihren gesamten auszuzahlenden Betrag spenden'
				except TypeError:
					try:
						if values["spendeMannTafel"] > 12:
							return 'Sie können maximal ihren gesamten auszuzahlenden Betrag spenden'
					except TypeError:
						try:
							if values["spendeMeerPlastik"] > 12:
								return 'Sie können maximal ihren gesamten auszuzahlenden Betrag spenden'
						except TypeError:
							try:
								if values["spendeWWF"] > 12:
									return 'Sie können maximal ihren gesamten auszuzahlenden Betrag spenden'
							except TypeError:
								pass
				 		
#		if self.player.spendeWWF is not None & self.player.spendeMeerPlastik is not None & self.player.spendeMannTafel is not None :
#			 if values["spendeWWF"] + values["spendeMeerPlastik"] + values["spendeMannTafel"] > self.participant.vars['pay']:
#			 	return 'Sie können maximal ihren gesamten auszuzahlenden Betrag spenden'
#		elif isinstance(self.player.spendeWWF, type(None))==False & isinstance(self.player.spendeMeerPlastik, type(None))==True & isinstance(self.player.spendeMannTafel, type(None))==True :
#			if values["spendeMeerPlastik"] + values["spendeMannTafel"] > self.participant.vars['pay']:
#				return 'Sie können maximal ihren gesamten auszuzahlenden Betrag spenden'
#		elif isinstance(self.player.spendeWWF, type(None))==True & isinstance(self.player.spendeMeerPlastik, type(None))==False & isinstance(self.player.spendeMannTafel, type(None))==True :
#			if values["spendeWWF"] + values["spendeMannTafel"] > self.participant.vars['pay']:
#				return 'Sie können maximal ihren gesamten auszuzahlenden Betrag spenden'
#		elif isinstance(self.player.spendeWWF, type(None))==True & isinstance(self.player.spendeMeerPlastik, type(None))==True & isinstance(self.player.spendeMannTafel, type(None))==False :
#			if values["spendeWWF"] + values["spendeMeerPlastik"] > self.participant.vars['pay']:
#				return 'Sie können maximal ihren gesamten auszuzahlenden Betrag spenden'
#		elif isinstance(self.player.spendeWWF, type(None))==False & isinstance(self.player.spendeMeerPlastik, type(None))==False & isinstance(self.player.spendeMannTafel, type(None))==True :
#			if values["spendeMannTafel"] > self.participant.vars['pay']:
#				return 'Sie können maximal ihren gesamten auszuzahlenden Betrag spenden'
#		elif isinstance(self.player.spendeWWF, type(None))==False & isinstance(self.player.spendeMeerPlastik, type(None))==True & isinstance(self.player.spendeMannTafel, type(None))==False :
#			if values["spendeMeerPlastik"]  > self.participant.vars['pay']:
#				return 'Sie können maximal ihren gesamten auszuzahlenden Betrag spenden'
#		elif isinstance(self.player.spendeWWF, type(None))==True & isinstance(self.player.spendeMeerPlastik, type(None))==False & isinstance(self.player.spendeMannTafel, type(None))==False :
#			if values["spendeWWF"] > self.participant.vars['pay']:
#				return 'Sie können maximal ihren gesamten auszuzahlenden Betrag spenden'
		


	def before_next_page(self):
		self.player.calc_payoff()





page_sequence = [
    MyPage
]
