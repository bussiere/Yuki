from datetime import datetime

from couchdbkit.ext.django.schema import *

class Author(Document):
	Name = StringProperty()
	Creation = DateTimeProperty(default=datetime.utcnow)

class Unit(Document):
	Name = StringProperty()
	Creation = DateTimeProperty(default=datetime.utcnow)

class Price(Document):
	Price = FloatProperty()
	Unit_Unit = ListProperty()
	Creation = DateTimeProperty(default=datetime.utcnow)
	Member_Member_Member = ListProperty()

class Figur(Document):
	Name = StringProperty()
	Character = StringProperty()
	Author_Author = ListProperty()
	Creation = DateTimeProperty(default=datetime.utcnow)
	Price_Price = ListProperty()
	Tag_Tag_Tag = ListProperty()
	def ___str__(self):
		return self.Name
	def __unicode__(self):
		return self.Name

class TypeMusic(Document):
	Type = StringProperty()
	Creation = DateTimeProperty(default=datetime.utcnow)

class Music(Document):
	TypeMusic_TypeMusic =  ListProperty()
	Name = StringProperty()
	Author = StringProperty()
	Date = DateTimeProperty()
	Price_Price = ListProperty()
	Creation = DateTimeProperty(default=datetime.utcnow)
	Tag_Tag_Tag = ListProperty()
	def ___str__(self):
		return self.Nom
	def __unicode__(self):
		return self.Nom

class TypeVideo(Document):
	Type = StringProperty()
	Creation = DateTimeProperty(default=datetime.utcnow)

class Video(Document):
	TypeVideo_TypeVideo = ListProperty()
	Name = StringProperty()
	Author_Author = ListProperty()
	Date = DateTimeProperty()
	Creation = DateTimeProperty(default=datetime.utcnow)
	Price_Price = ListProperty()
	Tag_Tag_Tag = ListProperty()
	def ___str__(self):
		return self.Nom
	def __unicode__(self):
		return self.Nom

class TypeVideoGame(Document):
	Type = StringProperty()
	Creation = DateTimeProperty(default=datetime.utcnow)

class VideoGame(Document):
	TypeVideoGame_TypeVideoGame = ListProperty()
	Name = StringProperty()
	Author_Author = ListProperty()
	Date = DateTimeProperty()
	Creation = DateTimeProperty(default=datetime.utcnow)
	Price_Price = ListProperty()
	Tag_Tag_Tag = ListProperty()
	def ___str__(self):
		return self.Nom
	def __unicode__(self):
		return self.Nom

class TypeBook(Document):
	Type = StringProperty()
	Creation = DateTimeProperty(default=datetime.utcnow)

class Book(Document):
	TypeBook_TypeBook = ListProperty()
	Name = StringProperty()
	Author_Author = ListProperty()
	Date = DateTimeProperty()
	Creation = DateTimeProperty(default=datetime.utcnow)
	Price_Price = ListProperty()
	Tag_Tag_Tag = ListProperty()
	def ___str__(self):
		return self.Nom
	def __unicode__(self):
		return self.Nom

class TypeGoodie(Document):
	Type = StringProperty()
	Creation = DateTimeProperty(default=datetime.utcnow)

class Goodie(Document):
	TypeGoodie_TypeGoodie = ListProperty()
	Name = StringProperty()
	Author_Author = ListProperty()
	Date = DateTimeProperty()
	Creation = DateTimeProperty(default=datetime.utcnow)
	Price_Price = ListProperty()
	Tag_Tag_Tag = ListProperty()
	def ___str__(self):
		return self.Nom
	def __unicode__(self):
		return self.Nom

# Create your models here.
class Item(Document):
	CodeBarre = StringProperty()
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
	