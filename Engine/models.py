from datetime import datetime

from couchdbkit.ext.django.schema import *


# Create your models here.
class Picture(Document):
	File = StringProperty()
	Creation = DateTimeProperty(default=datetime.utcnow)
	Member_Member = ListProperty()
	Item_Item = ListProperty()

	
	def ___str__(self):
		return self.Nom
	def __unicode__(self):
		return self.Nom

class Avatar(Document):
	File = StringProperty()
	Creation = DateTimeProperty(default=datetime.utcnow)
	Member_Member = ListProperty()
	Item_Item = ListProperty()
	def ___str__(self):
		return self.Nom
	def __unicode__(self):
		return self.Nom