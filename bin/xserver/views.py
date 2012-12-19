# Create your views here.
from django.http import HttpResponse 
from django.template.loader import get_template 
from django.template import Context, Template 
from django.shortcuts import render, RequestContext, render_to_response
from django.http import HttpResponse 
from form.models import LoginForm,VendeurForm,BarcodeForm,ItemForm,AvisForm
from engine.models import Item

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
    if request.method == 'POST': # If the form has been submitted...
        form = ItemForm(request.POST) # A form bound to the POST data
        if form.is_valid(): 
            barcode = form.cleaned_data['Barcode']
            nom = form.cleaned_data['Nom']
            description = form.cleaned_data['Description']
            tag = form.cleaned_data['Tag']
            vendeur = form.cleaned_data['Vendeur']
            image = form.cleaned_data['Image']
            demandeavis = form.cleaned_data['DemandeAvis']
            items = Item.objects.filter(Barcode__BarCode__contains=barcode)
            if (items) :
                for item in items :
                    if item.Nom == nom :
                        rendered = render_to_response('additem.html', {'truc': truc,'loginform': loginform,'itemform':itemform},context_instance=RequestContext(request))
            tag = tag.split(" ")
            # on recherche le code barre
            barcodeobject = Barcode.objects.filter(BarCode__exact=barcode)
            if not barcode :
                barcodeobject = Barcode.create(BarCode=barcode)
            # on recherche un item avec le meme nom
            itemobject = Barcode.objects.filter(BarCode__exact=barcode)
            result = barcode
    rendered = render_to_response('additem.html', {'truc': truc,'loginform': loginform,'itemform':itemform},context_instance=RequestContext(request))
    return  rendered


def  searchitem(request):
    truc = 'toto'
    loginform = LoginForm()
    avisform = AvisForm()
    result = None
    if request.method == 'POST': # If the form has been submitted...
        form = BarcodeForm(request.POST) # A form bound to the POST data
        if form.is_valid(): 
            barcode = form.cleaned_data['Barcode']
            barcode = Item.objects.filter(Barcode__BarCode__contains=barcode)
            result = barcode
    rendered = render_to_response('searchitem.html', {'result':result,'truc': truc,'loginform': loginform,'avisform':avisform},context_instance=RequestContext(request))
    return  rendered