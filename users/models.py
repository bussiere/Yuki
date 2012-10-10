from django.db import models
from django.contrib.auth.models import User
from fieldRangeField import IntegerRangeField
class IntegerRangeField(models.IntegerField):
    def __init__(self, verbose_name=None, name=None, min_value=None, max_value=None, **kwargs):
        self.min_value, self.max_value = min_value, max_value
        models.IntegerField.__init__(self, verbose_name, name, **kwargs)
    def formfield(self, **kwargs):
        defaults = {'min_value': self.min_value, 'max_value':self.max_value}
        defaults.update(kwargs)
        return super(IntegerRangeField, self).formfield(**defaults)

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
    Note = models.CharField(max_length=200,null=True,blank=True)
    Rank = IntegerRangeField(min_value=0, max_value=10)
