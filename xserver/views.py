# Create your views here.
from django.http import HttpResponse 
from django.template.loader import get_template 
from django.template import Context, Template 
from django.shortcuts import render, RequestContext, render_to_response
from django.http import HttpResponse 
from form.models import LoginForm,VendeurForm,BarcodeForm

def index(request):
    truc = 'toto'
    loginform = LoginForm()
    barcodeform = BarcodeForm()
    vendeurform =  VendeurForm()
    rendered = render_to_response('index.html', {'truc': truc,'loginform': loginform,'vendeurform':vendeurform,'barcodeform':barcodeform},context_instance=RequestContext(request))
    return  rendered