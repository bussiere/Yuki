from datetime import datetime

from couchdbkit.ext.django.schema import *

# Create your models here.

class Statut(Document):
	Nom= StringProperty()

class Member(Document):
	Nom= StringProperty()
	Note_divers_note_Note_divers = ListProperty()
	Inscription = DateTimeProperty(default=datetime.utcnow)
	Statut = ListProperty()
	Email = StringProperty()
	Vote_Vote = ListProperty()
	Tag_Tag = ListProperty()
	Avatar_Picture_Avatar = StringProperty()


	
	def ___str__(self):
		return self.Nom
	def __unicode__(self):
		return self.Nom