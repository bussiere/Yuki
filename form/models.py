from django.db import models
from django.shortcuts import render_to_response
from django.forms import ModelForm
from django import forms




class LoginForm(forms.Form):
	Email =  forms.EmailField(label="Email")
	Password = forms.CharField(label="Password", widget=forms.PasswordInput)

class BarcodeForm(forms.Form):
	Barcode = forms.CharField(label="Barcode")

class VendeurForm(forms.Form):
	Nom = forms.CharField(label="Nom")

class ItemForm(forms.Form):
	Barcode = forms.CharField(label="Barcode")
	Nom =  forms.CharField(label="Nom")
	Description = forms.CharField(label="Description")
	Vendeur = forms.CharField(label="Vendeur")
	Image = forms.ImageField(label="Image")
	DemandeAvis = forms.BooleanField(label="Demander un avis")
