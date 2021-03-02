from . import models
from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
import time



class Control1(Page):
	form_model=models.Player
	form_fields=["test_attempts","FE6"]

#	def error_message(self,values):
#		try:
#			if values["Q1_1"] + values["Q1_11"] !=4:
#				self.player.wrong_Q1_2 +=1
#				self.player.wrong+=1
#		except TypeError:
#			self.player.error1()
	def FE6_error_message(self,value):
		if not (str(value)==str(['4'])):
			self.player.wrong_Q1_1 +=1 
			self.player.wrong +=1
	
	def before_next_page(self):
		self.player.test_attempts+=1
		self.player.time()
				

class Instr1(Page):
	def is_displayed(self):
		return self.player.wrong_Q1_1 > 0
	def before_next_page(self):
		self.player.timin21()
		

class Control11(Page):
	def is_displayed(self):
		return self.player.wrong_Q1_1 == 1

	form_model=models.Player
	form_fields=["FE6"]

	def FE6_error_message(self,value):
		if not (str(value)==str(['4'])):
			self.player.wrong_Q1_1 +=1 
			self.player.wrong +=1

	def before_next_page(self):
		self.player.test_attempts+=1
		self.player.tim21()


class Instr11(Page):
	def is_displayed(self):
		return self.player.wrong_Q1_1 == 2
	def before_next_page(self):
		self.player.timin22()


class Control12(Page):
	def is_displayed(self):
		return self.player.wrong_Q1_1 > 1

	form_model=models.Player
	form_fields=["FE6"]

	def FE6_error_message(self,value):
		if not (str(value)==str(['4'])):
			self.player.wrong_Q1_1 +=1 
			self.player.wrong +=1
			return 'Hilfe: "Die Kapazität wird in Milli-Ampere-Stunden (mAh) angegeben und gibt an, wie viel Strom der Akku speichern kann. Die Entladung des Akkus wird in Milli-Ampere gemessen und hängt davon ab, wie energieintensiv ein Gerät ist. Milli-Ampere-Stunden geben also an, wie viele Stunden der Akku Strom liefert, wenn dieser mit einer Spannung von einem Milli-Ampere entladen wird. Wird eine höhere Spannung benötigt, verkürzt sich diese Zeit dementsprechend. Ist die Akkukapazität beispielsweise mit 1.000 mAh angegeben, so liefert der Akku eine Stunde lang 1.000 mA oder fünf Stunden lang 200 mA Strom."'

		#	if not (value==1):
#					return Falsch!!!!!!!!
#			def Q1_11_error_message(self,value):
#				if not (value==3):
#					return Falsch!!!!!!!!
		
	def before_next_page(self):
		self.player.test_attempts+=1
		self.player.tim22()


class Control2(Page):
	form_model=models.Player
	form_fields=["Q1_2"] 

	def Q1_2_error_message(self,value):
		if not (str(value)==str(['2','3'])):
			self.player.wrong_Q1_2 +=1 
			self.player.wrong +=1

	def before_next_page(self):
		self.player.test_attempts+=1
		self.player.tim3()


class Instr2(Page):
	def is_displayed(self):
		return self.player.wrong_Q1_2 > 0
	def before_next_page(self):
		self.player.timin31()
	


class Control21(Page):
	def is_displayed(self):
		return self.player.wrong_Q1_2 == 1

	form_model=models.Player
	form_fields=["Q1_2"]

	def Q1_2_error_message(self,value):
		if not (str(value)==str(['2','3'])):
			self.player.wrong_Q1_2 +=1 
			self.player.wrong +=1

	def before_next_page(self):
		self.player.test_attempts+=1
		self.player.tim31()

class Instr21(Page):
	def is_displayed(self):
		return self.player.wrong_Q1_2 == 2
	def before_next_page(self):
		self.player.timin32()


class Control22(Page):
	def is_displayed(self):
		return self.player.wrong_Q1_2 > 1

	form_model=models.Player
	form_fields=["Q1_2"]

	def Q1_2_error_message(self,value):
		if not (str(value)==str(['2','3'])):
			self.player.wrong_Q1_2 +=1 
			self.player.wrong +=1
			self.player.test_attempts+=1
			return 'Hilfe: "Die Auflösung wird in Anzahl an vertikalen und horizontalen Pixeln gemessen. Die SD Technologie hat eine Auflösung von maximal 720x576 Pixel, HD hat eine Auflösung von 1280x720 Pixel und 4K Technologie hat eine Auflösung von 4096x2160 Pixel."'
			

	def before_next_page(self):
		self.player.test_attempts+=1
		self.player.tim32()

		
class Control3(Page):
	form_model=models.Player
	form_fields=["Q1_3"]

	def Q1_3_error_message(self,value):
		if not (value==1):
			self.player.wrong_Q1_3 +=1 
			self.player.wrong +=1
	def before_next_page(self):
		self.player.test_attempts+=1
		self.player.tim4()

class Instr3(Page):
	def is_displayed(self):
		return self.player.wrong_Q1_3 == 1
	def before_next_page(self):
		self.player.timin41()


class Control31(Page):
	def is_displayed(self):
		return self.player.wrong_Q1_3 == 1

	form_model=models.Player
	form_fields=["Q1_3"]

	def Q1_3_error_message(self,value):
		if not (value==1):
			self.player.wrong_Q1_3 +=1 
			self.player.wrong +=1
	def before_next_page(self):
		self.player.test_attempts+=1
		self.player.tim41()

class Instr31(Page):
	def is_displayed(self):
		return self.player.wrong_Q1_3 == 2
	def before_next_page(self):
		self.player.timin42()

class Control32(Page):
	def is_displayed(self):
		return self.player.wrong_Q1_3 == 2

	form_model=models.Player
	form_fields=["Q1_3"]

	def Q1_3_error_message(self,value):
		if not (value==1):
			self.player.wrong +=1
			self.player.test_attempts+=1
			return 'Hilfe: "Ist die Akkukapazität beispielsweise mit 1.000 mAh angegeben, so liefert der Akku eine Stunde lang 1.000 mA oder fünf Stunden lang 200 mA Strom."'

	def before_next_page(self):
		self.player.test_attempts+=1
		self.player.tim42()

class Control4(Page):
	form_model=models.Player
	form_fields=["Q1_4"]

	def Q1_4_error_message(self,value):
		if not (value==3):
			self.player.wrong_Q1_4 +=1 
			self.player.wrong +=1

	def before_next_page(self):
		self.player.test_attempts+=1
		self.player.tim5()


class Instr4(Page):
	def is_displayed(self):
		return self.player.wrong_Q1_4 ==1
	def before_next_page(self):
		self.player.timin51()


class Control41(Page):
	def is_displayed(self):
		return self.player.wrong_Q1_4 == 1

	form_model=models.Player
	form_fields=["Q1_4"]

	def Q1_4_error_message(self,value):
		if not (value==3):
			self.player.wrong_Q1_4 +=1 
			self.player.wrong +=1
	def before_next_page(self):
		self.player.test_attempts+=1
		self.player.tim51()
			

class Instr41(Page):
	def is_displayed(self):
		return self.player.wrong_Q1_4 == 2
	def before_next_page(self):
		self.player.timin52()

class Control42(Page):
	def is_displayed(self):
		return self.player.wrong_Q1_4 == 2

	form_model=models.Player
	form_fields=["Q1_4"]

	def Q1_4_error_message(self,value):
		if not (value==3):
			self.player.wrong +=1
			self.player.test_attempts+=1
			return 'Hilfe: "Displaygrößen: 4 Zoll (9,8 cm), 5 Zoll (12,7cm) und 6 Zoll (15,24 cm)."'

	def before_next_page(self):
		self.player.test_attempts+=1
		self.player.tim52()

class Control5(Page):
	form_model=models.Player
	form_fields=["Q1_5"]

	def Q1_5_error_message(self,value):
		if not (value==4):
			self.player.wrong_Q1_5 +=1
			self.player.wrong +=1 
	def before_next_page(self):
		self.player.test_attempts+=1
		self.player.tim6()

class Instr5(Page):
	def is_displayed(self):
		return self.player.wrong_Q1_5 == 1
	def before_next_page(self):
		self.player.timin61()


class Control51(Page):
	def is_displayed(self):
		return self.player.wrong_Q1_5 == 1

	form_model=models.Player
	form_fields=["Q1_5"]

	def Q1_5_error_message(self,value):
		if not (value==4):
			self.player.wrong_Q1_5 +=1 
			self.player.wrong +=1
	def before_next_page(self):
		self.player.test_attempts+=1
		self.player.tim61()

class Instr51(Page):
	def is_displayed(self):
		return self.player.wrong_Q1_5 == 2
		

	def before_next_page(self):
		self.player.timin62()

class Control52(Page):
	def is_displayed(self):
		return self.player.wrong_Q1_5 == 2

	form_model=models.Player
	form_fields=["Q1_5"]

	def Q1_5_error_message(self,value):
		if not (value==4):
			self.player.wrong +=1
			self.player.test_attempts+=1
			return 'Hilfe: Gegeben, dass eine größere Akkukapazität, eine höhere Kameraauflösung und ein größeres Display besser sind, würde Antwortmöglichkeit 4 alle anderen dominieren.'

	def before_next_page(self):
		self.player.test_attempts+=1
		self.player.tim62()

class Feedback(Page):
	def before_next_page(self):
		self.player.tim7()




page_sequence = [
	Control1,
	Instr1,
	Control11,
	Instr11,
	Control12,
	Control2,
	Instr2,
	Control21,
	Instr21,
	Control22,
	Control3,
	Instr3,
	Control31,
	Instr31,
	Control32,
	Control4,
	Instr4,
	Control41,
	Instr41,
	Control42,
	Control5,
	Instr5,
	Control51,
	Instr51,
	Control52,
	Feedback
]
