from django.db import models

class Tag(models.Model):
    Nom = models.CharField(max_length=200,null=True,blank=True)
    def ___str__(self):
        return self.Nom
    def __unicode__(self):
        return self.Nom

class CategorieObject(models.Model):
    Nom = models.CharField(max_length=200,null=True,blank=True)
    def ___str__(self):
        return self.Nom
    def __unicode__(self):
        return self.Nom

class ImageObject(models.Model):
    Image = models.CharField(max_length=200,null=True,blank=True)
    def ___str__(self):
        return self.Nom
    def __unicode__(self):
        return self.Nom
class Object(models.Model):
    CategoryObject = models.ForeignKey('CategorieObject',null=True,blank=True)
    Tag =  models.ForeignKey('Tag',null=True,blank=True)
    Nom = models.CharField(max_length=200,null=True,blank=True)
    Description = models.CharField(max_length=300,null=True,blank=True)
    Image = models.ManyToManyField('ImageObject',null=True,blank=True)
    Note_divers = models.ManyToManyField('users.Note',null=True,blank=True)
    def ___str__(self):
        return self.Nom
    def __unicode__(self):
        return self.Nom
