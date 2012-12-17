from django.db import models
from django.contrib.auth.models import User
from fieldRangeField import IntegerRangeField

class Sentai(models.Model):
    RED = 'Red'
    ORANGE = 'Orange' 
    YELLOW = 'YELLOW'
    RANK = (
    (-1, RED),
    (0, ORANGE),
    (1, YELLOW),
    )
    User = models.ForeignKey(User, unique=True,null=True,blank=True) 
    Pseudo = models.CharField(max_length=200,null=True,blank=True)
    Email =  models.EmailField(null=True,blank=True)
    Date_inscription = models.DateTimeField('date inscription',null=True,blank=True)
    RankNote = IntegerRangeField(min_value=0, max_value=100)
    Rank = models.IntegerField(choices=RANK,default=RED)

class Note(models.Model):
    User = models.ForeignKey('Sentai', unique=True,null=True,blank=True) 
    NoteUser = models.CharField(max_length=200,null=True,blank=True)
    Rank = IntegerRangeField(min_value=0, max_value=10)
