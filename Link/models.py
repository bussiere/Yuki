from datetime import datetime
from couchdbkit.ext.django.schema import *
# Create your models here.
class CategorieLien(Document):
    Nom= StringProperty()
    Note_divers_note_Note_divers= ListProperty()
    Visibilite_visibilite_Visibilite= ListProperty()
class Lien(Document):
    Categorie_CategorieLien= ListProperty()
    Nom= StringProperty()
    url= StringProperty()
    alt= StringProperty()
    Texte_contenu_presentation_Texte_contenu= ListProperty()
    MiseEnForme_presentation_MiseEnForme= ListProperty()
    Note_divers_note_Note_divers= ListProperty()
    Visibilite_visibilite_Visibilite= ListProperty()
class LienFacebook(Document):
    LienFacaebook_Lien= ListProperty()
class LienTwitter(Document):
    LienTwitter_Lien= ListProperty()
class Admin:
    pass
