from datetime import datetime

from couchdbkit.ext.django.schema import *

# Create your models here.
class NomsEndroit(Document):
	Nom= StringProperty()

class Pays(Document):
    Nom_NomsEndroit
= ListProperty()

    
    GPS= StringProperty()

    GeoHash= StringProperty()

    
    GoogleMaps_lien_Lien= ListProperty()

    
    Liens_lien_Lien= ListProperty()

class Etat(Document):
	Nom_NomsEndroit
= ListProperty()

	GPS= StringProperty()

	GeoHash= StringProperty()

	GoogleMaps_lien_Lien= ListProperty()

	Liens_lien_Lien= ListProperty()

class Region(Document):
	Nom_NomsEndroit
= ListProperty()

	GPS= StringProperty()

	GeoHash= StringProperty()

	GoogleMaps_lien_Lien= ListProperty()

	Liens_lien_Lien= ListProperty()

class Ville(Document):
	Nom_NomsEndroit
= ListProperty()

	GPS= StringProperty()

	GeoHash= StringProperty()

	GoogleMaps_lien_Lien= ListProperty()

	Liens_lien_Lien= ListProperty()

class Adresse(Document):
	Numero= IntegerProperty()

	Nom_NomsEndroit
= ListProperty()

	GPS= StringProperty()

	GeoHash= StringProperty()

	GoogleMaps_lien_Lien= ListProperty()

	Liens_lien_Lien= ListProperty()

class Localisation(Document):
	GPS= StringProperty()

	GeoHash= StringProperty()

	GoogleMaps_lien_Lien= ListProperty()

	Liens_lien_Lien= ListProperty()

	Adresse_Adresse= ListProperty()

	ville_Ville= ListProperty()

	region_Region = ListProperty()

	etat_Etat = ListProperty()

	pays_pays = ListProperty()

	Tags_tag_Tag= ListProperty()

class Admin:

    pass
