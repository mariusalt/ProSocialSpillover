from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants



class Questionnaire(Page):
	form_model = models.Player
	form_fields = ['Deserving1','Deserving2','Realization','Env1','Env2','Env3','Env4','Env5','Env6','Env7','Env8','Env9','EnvIdent1','EnvIdent2','EnvIdent3','Efficacy1','Efficacy2','Efficacy3','Efficacy4','Deontologist1','Deontologist2','Deontologist3','Deontologist4','Donation1','Donation2','risk', 'exhaust1', 'gender','age', 'language', 'party','volun','Info','email']

class finish(Page):
	pass

page_sequence = [
   Questionnaire,
   finish
]
