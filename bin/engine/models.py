from django.db import models

# Create your models here.

class Item(models.Model):
	Barcode = models.ManyToManyField('barcode.BarCode',null=True,blank=True)
	Object = models.ForeignKey('object.Object',null=True,blank=True)
	Avis = models.ManyToManyField('avis.Avis',null=True,blank=True)
	Demande = models.BooleanField(default=False)