from django.db import models



class CategorieSeller(models.Model):
    Nom = models.CharField(max_length=200,null=True,blank=True)
    def ___str__(self):
        return self.Nom
    def __unicode__(self):
        return self.Nom

# Create your models here.
class Seller(models.Model):
    CategorySeller = models.ForeignKey('CategorieSeller',null=True,blank=True)
    Nom = models.CharField(max_length=200,null=True,blank=True)
    Adresse = models.CharField(max_length=200,null=True,blank=True)
    Email =  models.EmailField(null=True,blank=True)
    Telephone = models.CharField(max_length=200,null=True,blank=True)
    SiteWeb = models.CharField(max_length=600,null=True,blank=True)
    Lieu = models.ForeignKey('lieu.Lieu',null=True, blank=True)
    Note_divers = models.ManyToManyField('users.Note',null=True,blank=True)