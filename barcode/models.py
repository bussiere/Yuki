from django.db import models

# Create your models here.
class BarCode(models.Model):
    BarCode = models.CharField(max_length=200,null=True,blank=True)
    Note_divers = models.ManyToManyField('users.Note',null=True,blank=True)
    def ___str__(self):
        return self.Nom
    def __unicode__(self):
        return self.Nom

