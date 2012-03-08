from datetime import datetime

from couchdbkit.ext.django.schema import *

# Create your models here.
class Tag(Document):
     Nom = StringProperty()
     Creation= DateTimeProperty(default=datetime.utcnow)

class FamilleTag(Document):
    Nom= StringProperty()
    Tag_Tag = ListProperty()
    Creation= DateTimeProperty(default=datetime.utcnow)

class Asso_Tag(Document):
	Tag_Tag = ListProperty()
	FamilleTag_FamilleTag = ListProperty()
	Member_Member = ListProperty()

class Admin:

    pass
