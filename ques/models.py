from otree.api import (
	models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
	Currency as c, currency_range
)


author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
	name_in_url = 'ques'
	players_per_group = None
	num_rounds = 1


class Subsession(BaseSubsession):
	pass


class Group(BaseGroup):
	pass


class Player(BasePlayer):
	

	Deserving1 = models.PositiveIntegerField(
		choices=[
			[1, "Stimme überhaupt nicht zu"], 
			[2, "Stimme eher nicht zu"],
			[3, "Bin unentschieden"],
			[4, "Stimme eher zu"],
			[5, "Stimme voll und ganz zu"],
			[6, "Keine Angabe"]
		 ],
		 widget=widgets.RadioSelect)

	Deserving2 = models.PositiveIntegerField(
		choices=[
			[1, "Stimme überhaupt nicht zu"], 
			[2, "Stimme eher nicht zu"],
			[3, "Bin unentschieden"],
			[4, "Stimme eher zu"],
			[5, "Stimme voll und ganz zu"],
			[6, "Keine Angabe"]
		 ],
		 widget=widgets.RadioSelect)

	volun = models.PositiveIntegerField(
		choices=[
			[1, '0 gar nicht risikobereit'], 
			[2, '1'],
			[3, '2'],
			[4, "3"],
			[5, "4"],
			[6, "5"],
			[7, "6"],
			[8, "7"],
			[9, "8"],
			[10, "9"],
			[11, "10 sehr risikobereit"]
		 ],
		 label="Wie schätzen Sie sich persönlich ein: Sind Sie im Allgemeinen ein risikobereiter Mensch oder versuchen Sie, Risiken zu vermeiden? Bitte kruezen Sie ein Kästchen auf der Skala an, wobei der Wert 0 bedeutet: 'gar nicht risikobereit' und der Wert 10: 'sehr risikobereit'. Mit den Werten dazwischen können Sie Ihre Einschätzung abstufen.",
		 widget=widgets.RadioSelectHorizontal)

	Realization = models.PositiveIntegerField(
		choices=[
			[1, "Stimme überhaupt nicht zu"], 
			[2, "Stimme eher nicht zu"],
			[3, "Bin unentschieden"],
			[4, "Stimme eher zu"],
			[5, "Stimme voll und ganz zu"],
			[6, "Keine Angabe"]
		 ],
		 widget=widgets.RadioSelect)

	Env1 = models.PositiveIntegerField(
		choices=[
			[1, "Stimme überhaupt nicht zu"], 
			[2, "Stimme eher nicht zu"],
			[3, "Bin unentschieden"],
			[4, "Stimme eher zu"],
			[5, "Stimme voll und ganz zu"],
			[6, "Keine Angabe"]
		 ],
		 widget=widgets.RadioSelect)

	Env2 = models.PositiveIntegerField(
		choices=[
			[1, "Stimme überhaupt nicht zu"], 
			[2, "Stimme eher nicht zu"],
			[3, "Bin unentschieden"],
			[4, "Stimme eher zu"],
			[5, "Stimme voll und ganz zu"],
			[6, "Keine Angabe"]
		 ],
		 widget=widgets.RadioSelect)

	Env3 = models.PositiveIntegerField(
		choices=[
			[1, "Stimme überhaupt nicht zu"], 
			[2, "Stimme eher nicht zu"],
			[3, "Bin unentschieden"],
			[4, "Stimme eher zu"],
			[5, "Stimme voll und ganz zu"],
			[6, "Keine Angabe"]
		 ],
		 widget=widgets.RadioSelect)

	Env4 = models.PositiveIntegerField(
		choices=[
			[1, "Stimme überhaupt nicht zu"], 
			[2, "Stimme eher nicht zu"],
			[3, "Bin unentschieden"],
			[4, "Stimme eher zu"],
			[5, "Stimme voll und ganz zu"],
			[6, "Keine Angabe"]
		 ],
		 widget=widgets.RadioSelect)

	Env5 = models.PositiveIntegerField(
		choices=[
			[1, "Stimme überhaupt nicht zu"], 
			[2, "Stimme eher nicht zu"],
			[3, "Bin unentschieden"],
			[4, "Stimme eher zu"],
			[5, "Stimme voll und ganz zu"],
			[6, "Keine Angabe"]
		 ],
		 widget=widgets.RadioSelect)

	Env6 = models.PositiveIntegerField(
		choices=[
			[1, "Stimme überhaupt nicht zu"], 
			[2, "Stimme eher nicht zu"],
			[3, "Bin unentschieden"],
			[4, "Stimme eher zu"],
			[5, "Stimme voll und ganz zu"],
			[6, "Keine Angabe"]
		 ],
		 widget=widgets.RadioSelect)

	Env7 = models.PositiveIntegerField(
		choices=[
			[1, "Stimme überhaupt nicht zu"], 
			[2, "Stimme eher nicht zu"],
			[3, "Bin unentschieden"],
			[4, "Stimme eher zu"],
			[5, "Stimme voll und ganz zu"],
			[6, "Keine Angabe"]
		 ],
		 widget=widgets.RadioSelect)

	Env8 = models.PositiveIntegerField(
		choices=[
			[1, "Stimme überhaupt nicht zu"], 
			[2, "Stimme eher nicht zu"],
			[3, "Bin unentschieden"],
			[4, "Stimme eher zu"],
			[5, "Stimme voll und ganz zu"],
			[6, "Keine Angabe"]
		 ],
		 widget=widgets.RadioSelect)

	Env9 = models.PositiveIntegerField(
		choices=[
			[1, "Stimme überhaupt nicht zu"], 
			[2, "Stimme eher nicht zu"],
			[3, "Bin unentschieden"],
			[4, "Stimme eher zu"],
			[5, "Stimme voll und ganz zu"],
			[6, "Keine Angabe"]
		 ],
		 widget=widgets.RadioSelect)

	EnvIdent1 = models.PositiveIntegerField(
		choices=[
			[1, 'Sehr wichtig'], 
			[2, 'Wichitg'],
			[3, 'Nicht wichtig'],
			[4, "Überhaupt nicht wichtig"],
			[5, "Keine Angabe"]
		 ],
		 label="Wie wichtig ist Ihnen das Wohlergehen der Umwelt?",
		 widget=widgets.RadioSelect)


	EnvIdent2 = models.PositiveIntegerField(
		choices=[
			[1, 'Trifft voll und ganz zu'], 
			[2, 'Trifft zu'],
			[3, 'weder noch'],
			[4, 'trifft nicht zu'],
			[5, 'Trifft ganz und gar nicht zu'],
			[6, 'Keine Angabe']
		 ],
		 label="Umweltfreundliches Verhalten ist ein wichtiger Teil von dem was mich ausmacht.",
		 widget=widgets.RadioSelect)

	EnvIdent3 = models.PositiveIntegerField(
		choices=[
			[1, 'Trifft voll und ganz zu'], 
			[2, 'Trifft zu'],
			[3, 'weder noch'],
			[4, "trifft nicht zu"],
			[5, "Trifft ganz und gar nicht zu"],
			[6, "Keine Angabe"]
		 ],
		 label="Ich versuche durch mein Handeln (z.B. Konsum) negative Auswirkungen auf die Umwelt zu minimieren",
		 widget=widgets.RadioSelect)

	Efficacy1 = models.PositiveIntegerField(
		choices=[
			[1, 'Trifft voll und ganz zu'], 
			[2, 'Trifft zu'],
			[3, 'weder noch'],
			[4, "trifft nicht zu"],
			[5, "Trifft ganz und gar nicht zu"],
			[6, "Keine Angabe"]
		 ],
		 label="Ich definiere mich selbst als umweltbewusste Person.",
		 widget=widgets.RadioSelect)

	Efficacy2 = models.PositiveIntegerField(
		choices=[
			[1, 'Trifft voll und ganz zu'], 
			[2, 'Trifft zu'],
			[3, 'weder noch'],
			[4, "trifft nicht zu"],
			[5, "Trifft ganz und gar nicht zu"],
			[6, "Keine Angabe"]
		 ],
		 label="Ich definiere mich selbst als umweltbewusste Person.",
		 widget=widgets.RadioSelect)

	Efficacy3 = models.PositiveIntegerField(
		choices=[
			[1, 'Trifft voll und ganz zu'], 
			[2, 'Trifft zu'],
			[3, 'weder noch'],
			[4, "trifft nicht zu"],
			[5, "Trifft ganz und gar nicht zu"],
			[6, "Keine Angabe"]
		 ],
		 label="Ich definiere mich selbst als umweltbewusste Person.",
		 widget=widgets.RadioSelect)

	Efficacy4 = models.PositiveIntegerField(
		choices=[
			[1, 'Trifft voll und ganz zu'], 
			[2, 'Trifft zu'],
			[3, 'weder noch'],
			[4, "trifft nicht zu"],
			[5, "Trifft ganz und gar nicht zu"],
			[6, "Keine Angabe"]
		 ],
		 label="Ich definiere mich selbst als umweltbewusste Person.",
		 widget=widgets.RadioSelect)

	Deontologist1 = models.PositiveIntegerField(
		choices=[
			[1, "Stimme überhaupt nicht zu"], 
			[2, "Stimme eher nicht zu"],
			[3, "Bin unentschieden"],
			[4, "Stimme eher zu"],
			[5, "Stimme voll und ganz zu"],
			[6, "Keine Angabe"]
		 ],
		 widget=widgets.RadioSelect)

	Deontologist2 = models.PositiveIntegerField(
		choices=[
			[1, "Stimme überhaupt nicht zu"], 
			[2, "Stimme eher nicht zu"],
			[3, "Bin unentschieden"],
			[4, "Stimme eher zu"],
			[5, "Stimme voll und ganz zu"],
			[6, "Keine Angabe"]
		 ],
		 widget=widgets.RadioSelect)

	Deontologist3 = models.PositiveIntegerField(
		choices=[
			[1, "Stimme überhaupt nicht zu"], 
			[2, "Stimme eher nicht zu"],
			[3, "Bin unentschieden"],
			[4, "Stimme eher zu"],
			[5, "Stimme voll und ganz zu"],
			[6, "Keine Angabe"]
		 ],
		 widget=widgets.RadioSelect)

	Deontologist4 = models.PositiveIntegerField(
		choices=[
			[1, "Stimme überhaupt nicht zu"], 
			[2, "Stimme eher nicht zu"],
			[3, "Bin unentschieden"],
			[4, "Stimme eher zu"],
			[5, "Stimme voll und ganz zu"],
			[6, "Keine Angabe"]
		 ],
		 widget=widgets.RadioSelect)

	Donation1 = models.PositiveIntegerField(
		choices=[
			[1, 'Ja'], 
			[2, 'Nein'],
			[3, 'Keine Angabe']
		 ],
		 label="Haben Sie im letzten Jahr Spenden über 10€ getätigt?",
		 widget=widgets.RadioSelect)

	Donation2 = models.StringField(
		initial=0,
		blank=True)

	risk = models.PositiveIntegerField(
		choices=[
			[1, '0 gar nicht risikobereit'], 
			[2, '1'],
			[3, '2'],
			[4, "3"],
			[5, "4"],
			[6, "5"],
			[7, "6"],
			[8, "7"],
			[9, "8"],
			[10, "9"],
			[11, "10 sehr risikobereit"]
		 ],
		 label="Wie schätzen Sie sich persönlich ein: Sind Sie im Allgemeinen ein risikobereiter Mensch oder versuchen Sie, Risiken zu vermeiden? Bitte kruezen Sie ein Kästchen auf der Skala an, wobei der Wert 0 bedeutet: 'gar nicht risikobereit' und der Wert 10: 'sehr risikobereit'. Mit den Werten dazwischen können Sie Ihre Einschätzung abstufen.",
		 widget=widgets.RadioSelectHorizontal)
	
	exhaust1 = models.PositiveIntegerField(
		choices=[
			[1, 'Sehr anstrengend'], 
			[2, 'Eher anstrengend'],
			[3, 'Wenig anstrengend'],
			[4, "Überhaupt nicht anstrengend"],
			[5, "Keine Angabe"]			
		 ],
		 label="Wie anstrengend empfanden Sie die Dekodierungsaufgabe in Teil 1?",
		 widget=widgets.RadioSelect)

	tippen = models.StringField(
		choices=['Sehr vertraut', 'Vertraut', 'Eher nicht vertraut', 'Gar nicht vertraut','Keine Angabe'],
		label="Wie schnell können Sie einen Text per Tastatur eingeben?",
		widget=widgets.RadioSelect)

	tenf = models.StringField(
		choices=['Ja', 'Nein', 'keine Angabe'],
		label="Beherrschen Sie das Zehnfinger-Schreibsystem?",
		widget=widgets.RadioSelect)

	gender = models.CharField(
		choices=['weiblich', 'männlich', 'weitere', 'keine Angabe'],
		label="Bitte geben Sie ihr Geschlecht an.",
		widget=widgets.RadioSelectHorizontal)

	age = models.PositiveIntegerField(label="Wie alt sind Sie?")

	nationality = models.CharField(label="Was ist Ihre Staatsangehörigkeit?")

	language = models.CharField(label="Welche Muttersprache(n) sprechen Sie?")

	party = models.PositiveIntegerField(
		choices=[
			[1, 'CDU/CSU'], 
			[2, 'SPD'],
			[3, 'AfD'],
			[4, "FDP"],
			[5, "Bündnis 90/Die Grünen"],
			[6, "Die Linke"],
			[7, "andere"],
			[8, "Keine Angabe"]
		 ],
		 label="Welche Partei würden Sie wählen, wenn am nächsten Sonntag Bundestagswahl wäre?",
		 widget=widgets.RadioSelect)

	education = models.PositiveIntegerField(
		choices=[
			[1, 'Keinen Schulabschluss'], 
			[2, 'Hauptschulabschluss'],
			[3, 'Mittlere Reife'],
			[4, "Abitur"],
			[5, "Abgeschlossene Ausbildung"],
			[6, "Univeritäts- / Fachhochschulabschluss"],
			[7, "Promotion"],
			[9, "Keine Angabe"]
		 ],
		 label="Was ist Ihr höchster Bildungsabschluss?",
		 widget=widgets.RadioSelect)
	

	occupation = models.CharField(label="Welchen Beruf üben Sie aus?")
	Info=models.IntegerField()
	email = models.StringField(blank=True)


