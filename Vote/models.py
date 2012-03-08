from datetime import datetime

from couchdbkit.ext.django.schema import *

# Create your models here.

class VoteHK(Document):
	Creation = DateTimeProperty(default=datetime.utcnow)
	Member_Member = ListProperty()
	def ___str__(self):
		return self.Nom
	def __unicode__(self):
		return self.Nom

class VoteNonHK(Document):
	Creation = DateTimeProperty(default=datetime.utcnow)
	Member_Member = ListProperty()
	def ___str__(self):
		return self.Nom
	def __unicode__(self):
		return self.Nom

class Vote(Document):
	VoteHK_VoteHK = ListProperty()
	VoteNonHK_VoteNonHK = ListProperty()
	Count = IntegerProperty()
	def ___str__(self):
		return self.Nom
	def __unicode__(self):
		return self.Nom
	