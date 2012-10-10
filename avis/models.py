from django.db import models

# Create your models here.

class Avis(models.Model):
	HK = 'HK'
	UNKNOWN = 'Unknown' 
	NONHK = 'Non Hk'
	NOTEHK = (
    (-1, HK),
    (0, UNKNOWN),
    (1, NOTEHK),)
	Rank = models.IntegerField(choices=NOTEHK,default=UNKNOWN)
    User = .ManyToManyField('users.User',null=True,blank=True)
    Note_divers = models.ManyToManyField('users.Note',null=True,blank=True)
    def ___str__(self):
        return self.Nom
    def __unicode__(self):
        return self.Nom
