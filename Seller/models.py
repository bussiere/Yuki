from datetime import datetime

from couchdbkit.ext.django.schema import *

class Seller(Document):
	Name = StringProperty()
	Localisation_Localisation_Localisation = ListProperty()
	Creation = DateTimeProperty(default=datetime.utcnow)
	Figur_Figur = ListProperty()
	Book_Book = ListProperty()
	Music_Music = ListProperty()
	VideoGame_VideoGame = ListProperty()
	Book_Book = ListProperty()
	Goodie_Goodie = ListProperty()
	Vote_Vote_Vote = ListProperty()
	Seller_Seller_Seller = ListProperty()
	Tag_Tag_Tag = ListProperty()
	def ___str__(self):
		return self.Nom
	def __unicode__(self):
		return self.Nom