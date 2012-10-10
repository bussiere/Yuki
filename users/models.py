from django.db import models

class Client(models.Model):
    User = models.ForeignKey(User, unique=True,null=True,blank=True) 
    Pseudo = models.CharField(max_length=200,null=True,blank=True)
    Email =  models.EmailField(null=True,blank=True)
    Date_inscription = models.DateTimeField('date inscription',null=True,blank=True)
    Rank = fieldRangeField.IntegerRangeField(min_value=0, max_value=100)