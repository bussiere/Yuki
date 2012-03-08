import os
chemin = "C:/Users/Bussiere/Dropbox/Projets/jackpoint/jackpoint"

#(,
#(models.Model)
#(null=True,blank=True)
#models.NullBooleanField(blank=True)
#models.BooleanField(null=True,blank=True)
def flistemodel(chemin):
    listfile =  os.listdir(chemin) 
    listemodel = []
    for f in listfile :
        if os.path.isdir(os.path.join(chemin, f)):
            listindir =  os.listdir(os.path.join(chemin, f)) 
            for f2 in listindir :
                if f2 == "models.py":
                    listemodel.append(os.path.join(chemin, f,f2))
    return listemodel


def replacemodel(ligne):
    ligne = ligne.replace(")",",null=True,blank=True)")
    ligne = ligne.replace("models.Model,null=True,blank=True","models.Model")
    ligne = ligne.replace("(,","(")
    ligne = ligne.replace("self,null=True,blank=True","self")
    ligne = ligne.replace("models.BooleanField(null=True,blank=True)","models.NullBooleanField(blank=True)")
    ligne = ligne.replace("models.BooleanField(null=True,blank=True)","models.NullBooleanField(blank=True)")
    ligne = ligne.replace("null=True,blank=True,null=True,blank=True","null=True,blank=True")
    return ligne


def searchblank(ligne,count):
    result = False
    if ligne == "\r\n":
        count += 1
        result = True
    return [count,result]

def replacemodel2(ligne,m):
    if ligne == "\r" :
        ligne = ""
    if ligne == "\n":
        ligne = ""
    if ligne == "\r\n":
        ligne = ""
#    ligne = ligne.replace(" =","=")
#    lignetab = ligne.split("=")
#    ligne = ligne.replace("models.Model","Document")
#    ligne = ligne.replace("from django.db import models","""from datetime import datetime\r\nfrom couchdbkit.ext.django.schema import *\r\n""")
#    if ligne.find("ManyToManyField") != -1 :
#        field = lignetab[1].split("(")
#        try :
#            field = field[1].split(",")[0]
#        except :
#            field = field[0]
#        droite =  field.replace("'","")
#        droite =  droite.replace(".","_")
#        droite = droite.replace(")","")
#        droite = droite.replace(" ","")
#        ligne =  lignetab[0]+"_"+ droite + " = ListProperty()" 
#    if ligne.find("models.CharField") != -1 :
#        ligne = lignetab[0] + " = StringProperty()"
#    if ligne.find("models.FloatField") != -1 :
#        ligne = lignetab[0] + " = FloatProperty()" 
#    if ligne.find("models.BooleanField") != -1 :
#        ligne = lignetab[0] + " = BooleanProperty()"
#    if ligne.find("models.EmailField") != -1 :
#        ligne = lignetab[0] + " = StringProperty()"
#    if ligne.find("models.IntegerField") != -1 :
#        ligne = lignetab[0] + " = IntegerProperty()"    
#    if ligne.find("DateTimeField") != -1 :
#        ligne = lignetab[0] + " = DateTimeProperty(default=datetime.utcnow)"
#    print m
#    print ligne
    return ligne#+"\r\n"
        



listemodel = flistemodel(chemin)
for m in listemodel :
    total = ""
    f = open(m, 'r')
    for t in f : 
        print m
        t = replacemodel2(t,m)
        total += t
    f.close()
    f = open(m, 'w')
    f.write(total)
    f.close()