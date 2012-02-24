from datetime import datetime

from couchdbkit.ext.django.schema import *

# Create your models here.
class Categorie_Page(Document):
	Nom= StringProperty()

	Note_divers_note_Note_divers= ListProperty()

	
	def ___str__(self):
		return self.Nom
	def __unicode__(self):
		return self.Nom
class Template(Document):
	Nom= StringProperty()

	contenu= models. TextField(max_length=80000, blank=True)
	Note_divers_note_Note_divers= ListProperty()

	def ___str__(self):
		return self.Nom
	def __unicode__(self):
		return self.Nom
class Page(Document):
    Template_Template= ListProperty()

    self_url_lien_Lien= ListProperty()

    Categorie_Categorie_Page= ListProperty()

    Liens_lien_Lien= ListProperty()

    Nom= StringProperty()

    ImagesSite_presentation_ImageSite= ListProperty()

    Texte_contenu_presentation_Texte_contenu= ListProperty()

    Note_divers_note_Note_divers= ListProperty()

    MiseEnForme_presentation_MiseEnForme= ListProperty()

    Menu_presentation_Menu= ListProperty()

    Notation_notation_Notation= ListProperty()

    Regle_regles_Regle= ListProperty()

    generated= DateTimeProperty(default=datetime.utcnow)

    modified= DateTimeProperty(default=datetime.utcnow)

    protege= BooleanProperty()

    def ___str__(self):
        return self.Nom
    def __unicode__(self):
        return self.Nom
class Admin:

    pass
