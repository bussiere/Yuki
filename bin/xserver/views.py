# Create your views here.
from django.http import HttpResponse 
from django.template.loader import get_template 
from django.template import Context, Template 
from django.shortcuts import render, RequestContext, render_to_response
from django.http import HttpResponse 
from form.models import LoginForm,VendeurForm,BarcodeForm,ItemForm,AvisForm

def index(request):
    truc = 'toto'
    loginform = LoginForm()
    barcodeform = BarcodeForm()
    vendeurform =  VendeurForm()
    rendered = render_to_response('index.html', {'truc': truc,'loginform': loginform,'vendeurform':vendeurform,'barcodeform':barcodeform},context_instance=RequestContext(request))
    return  rendered

def additem(request):
    truc = 'toto'
    loginform = LoginForm()
    itemform = ItemForm()
    rendered = render_to_response('additem.html', {'truc': truc,'loginform': loginform,'itemform':itemform},context_instance=RequestContext(request))
    return  rendered


def  searchitem(request):
    truc = 'toto'
    loginform = LoginForm()
    avisform = AvisForm()
    result = ""
    if request.method == 'POST': # If the form has been submitted...
        form = BarcodeForm(request.POST) # A form bound to the POST data
        if form.is_valid(): 
            barcode = form.cleaned_data['Barcode']
            result = barcode
    rendered = render_to_response('searchitem.html', {'result':result,'truc': truc,'loginform': loginform,'avisform':avisform},context_instance=RequestContext(request))
    return  rendered