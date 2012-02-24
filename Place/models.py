from datetime import datetime
from couchdbkit.ext.django.schema import *
# Create your models here.
class Avis(Document):
	Texte= StringProperty()
	Membre_membre_Membre= ListProperty()
	Publiable= models.NullBooleanField(blank=True)
	Lien_lien_Lien= ListProperty()
	Note_divers_note_Note_divers= ListProperty()
	Geohash= StringProperty()
	Tags_tag_Tag= ListProperty()
class TypeLieux(Document):
	Nom= StringProperty()
	Tags_tag_Tag= ListProperty()
class Lieux(Document):
	Localisation_localisation_Localisation= ListProperty()
	Texte= StringProperty()
	Notation_notation_Notation= ListProperty()
	Liens_lien_Lien= ListProperty()
	Horaire_horaire_Horaire= ListProperty()
	Tags_tag_Tag= ListProperty()
	Note_note_Note_divers= ListProperty()
class Admin:
    pass
