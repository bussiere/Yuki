# -*- coding: utf-8 -*-

#########################################################################
## This scaffolding model makes your app work on Google App Engine too
## File is released under public domain and you can use without limitations
#########################################################################

## if SSL/HTTPS is properly configured and you want all HTTP requests to
## be redirected to HTTPS, uncomment the line below:
# request.requires_https()

if not request.env.web2py_runtime_gae:
    ## if NOT running on Google App Engine use SQLite or other DB
    db = DAL('sqlite://storage.sqlite')
else:
    ## connect to Google BigTable (optional 'google:datastore://namespace')
    db = DAL('google:datastore')
    ## store sessions and tickets there
    session.connect(request, response, db = db)
    ## or store session in Memcache, Redis, etc.
    ## from gluon.contrib.memdb import MEMDB
    ## from google.appengine.api.memcache import Client
    ## session.connect(request, response, db = MEMDB(Client()))

## by default give a view/generic.extension to all actions from localhost
## none otherwise. a pattern can be 'controller/function.extension'
response.generic_patterns = ['*'] if request.is_local else []
## (optional) optimize handling of static files
# response.optimize_css = 'concat,minify,inline'
# response.optimize_js = 'concat,minify,inline'

#########################################################################
## Here is sample code if you need for
## - email capabilities
## - auth_userentication (registration, login, logout, ... )
## - auth_userorization (role based auth_userorization)
## - services (xml, csv, json, xmlrpc, jsonrpc, amf, rss)
## - old style crud actions
## (more options discussed in gluon/tools.py)
#########################################################################

from gluon.tools import Auth, Crud, Service, PluginManager, prettydate
auth = Auth(db, hmac_key=Auth.get_or_create_key())
crud, service, plugins = Crud(db), Service(), PluginManager()

## create all tables needed by auth_user if not custom tables
auth.define_tables()


db.define_table('Barcode',
   Field('Barcode', unique=True),
   Field('auth_user','list:reference auth_user'),
   Field('Comment','list:reference Comment'),
   Field('Seller','list:reference Seller'),
   Field('Livre','list:reference Livre'),
   Field('Musique','list:reference Musique'),
   Field('Video','list:reference Video'),
   Field('Figur','list:reference Figur'),
   Field('Goodie','list:reference Goodie'),
   Field('VideoGame','list:reference VideoGame'),
   format = '%(Barcodee)s')
   
db.define_table('Comment',
   Field('Name', unique=True),
   Field('Texte'),
   Field('Vote', 'integer'),
   Field('auth_user',db.auth_user),
   format = '%(Name)s')


db.define_table('Convention',
   Field('Nom', unique=True),
   Field('Localisation','list:reference Localisation'),
   Field('auth_user','list:reference auth_user'),
   Field('Comment','list:reference Comment'),
   Field('Seller','list:reference Seller'),
   Field('Livre','list:reference Livre'),
   Field('Musique','list:reference Musique'),
   Field('Video','list:reference Video'),
   Field('Figur','list:reference Figur'),
   Field('Goodie','list:reference Goodie'),
   Field('Link','list:reference Link'),
   Field('Tag','list:reference Tag'),

   format = '%(Nom)s')

db.define_table('auth_useror',
   Field('Nom', unique=True),
   Field('Tag','list:reference Tag'),
   format = '%(Nom)s')

db.define_table('Character',
   Field('Nom', unique=True),
   Field('Tag','list:reference Tag'),
   format = '%(Nom)s')

db.define_table('Figur',
   Field('Name', unique=True),
   Field('Date'),
   Field('Characters','list:reference Character'),
   Field('auth_userors','list:reference auth_useror'),
   Field('Tag','list:reference Tag'),
   Field('Price','list:reference Price'),
   Field('Seller','list:reference Seller'),
   Field('Convention','list:reference Convention'),
   Field('Vote','list:reference Vote'),
   Field('BarCode','list:reference BarCode'),
   Field('Comment','list:reference Comment'),
   Field('Link','list:reference Link'),
   format = '%(Nom)s')
   
db.define_table('TypeMusic',
   Field('Nom', unique=True),
   format = '%(Nom)s')


db.define_table('Music',
   Field('Name', unique=True),
   Field('Date'),
   Field('auth_userors','list:reference auth_useror'),
   Field('Tag','list:reference Tag'),
   Field('Price','list:reference Price'),
   Field('Seller','list:reference Seller'),
   Field('Convention','list:reference Convention'),
   Field('Vote','list:reference Vote'),
   Field('BarCode','list:reference BarCode'),
   Field('Comment','list:reference Comment'),
   Field('Link','list:reference Link'),
   format = '%(Nom)s')


db.define_table('TypeVideo',
   Field('Nom', unique=True),
   format = '%(Nom)s')


db.define_table('Video',
   Field('Name', unique=True),
   Field('Date'),
   Field('auth_userors','list:reference auth_useror'),
   Field('Tag','list:reference Tag'),
   Field('Price','list:reference Price'),
   Field('Seller','list:reference Seller'),
   Field('Convention','list:reference Convention'),
   Field('Vote','list:reference Vote'),
   Field('BarCode','list:reference BarCode'),
   Field('Comment','list:reference Comment'),
   Field('Link','list:reference Link'),  
   format = '%(Nom)s')

db.define_table('TypeVideoGame',
   Field('Nom', unique=True),
   format = '%(Nom)s')


db.define_table('VideoGame',
   Field('Name', unique=True),
   Field('Date'),
   Field('auth_userors','list:reference auth_useror'),
   Field('Tag','list:reference Tag'),
   Field('Price','list:reference Price'),
   Field('Seller','list:reference Seller'),
   Field('Convention','list:reference Convention'),
   Field('Vote','list:reference Vote'),
   Field('BarCode','list:reference BarCode'),
   Field('Comment','list:reference Comment'),
   Field('Link','list:reference Link'),
   format = '%(Nom)s')

db.define_table('TypeBook',
   Field('Nom', unique=True),
   format = '%(Nom)s')


db.define_table('Book',
   Field('Name', unique=True),
   Field('Date'),
   Field('auth_userors','list:reference auth_useror'),
   Field('Tag','list:reference Tag'),
   Field('Price','list:reference Price'),
   Field('Seller','list:reference Seller'),
   Field('Convention','list:reference Convention'),
   Field('Vote','list:reference Vote'),
   Field('BarCode','list:reference BarCode'),
   Field('Comment','list:reference Comment'),
   Field('Link','list:reference Link'),
   format = '%(Nom)s')


db.define_table('TypeGoodie',
   Field('Nom', unique=True),
   format = '%(Nom)s')


db.define_table('Goodie',
   Field('Name', unique=True),
   Field('Date'),
   Field('auth_userors','list:reference auth_useror'),
   Field('Tag','list:reference Tag'),
   Field('Price','list:reference Price'),
   Field('Seller','list:reference Seller'),
   Field('Convention','list:reference Convention'),
   Field('Vote','list:reference Vote'),
   Field('BarCode','list:reference BarCode'),
   Field('Comment','list:reference Comment'),
   Field('Link','list:reference Link'),
   format = '%(Nom)s')



db.define_table('GPS',
   Field('GPS', unique=True),
   Field('Tag','list:reference Tag'),
   format = '%(GPS)s')

db.define_table('GeoHash',
   Field('GeoHash', unique=True),
   Field('Tag','list:reference Tag'),
   format = '%(GeoHash)s')

db.define_table('OpenStreetMap',
   Field('OpenStreetMap', unique=True),
   Field('Tag','list:reference Tag'),
   format = '%(OpenStreetMap)s')

db.define_table('Country',
   Field('Name', unique=True),
   Field('Link','list:reference Link'),
   Field('GPS','list:reference GPS'),
   Field('GeoHash','list:reference GeoHash'),
   Field('OpenStreetMap','list:reference OpenStreetMap'),
   format = '%(Name)s')
   
db.define_table('State',
   Field('Name', unique=True),
   Field('Link','list:reference Link'),
   Field('GPS','list:reference GPS'),
   Field('GeoHash','list:reference GeoHash'),
   Field('OpenStreetMap','list:reference OpenStreetMap'),
   format = '%(Name)s')
   

db.define_table('Region',
   Field('Name', unique=True),
   Field('Link','list:reference Link'),
   Field('GPS','list:reference GPS'),
   Field('GeoHash','list:reference GeoHash'),
   Field('OpenStreetMap','list:reference OpenStreetMap'),
   format = '%(Name)s')
   
 
db.define_table('City',
   Field('Name', unique=True),
   Field('Link','list:reference Link'),
   Field('GPS','list:reference GPS'),
   Field('GeoHash','list:reference GeoHash'),
   Field('OpenStreetMap','list:reference OpenStreetMap'),
   format = '%(Name)s')

db.define_table('Adress',
   Field('Name', unique=True),
   Field('Number', unique=True),
   Field('Link','list:reference Link'),
   Field('GPS','list:reference GPS'),
   Field('GeoHash','list:reference GeoHash'),
   Field('OpenStreetMap','list:reference OpenStreetMap'),
   format = '%(Name)s')
   
db.define_table('PostalCode',
   Field('Name', unique=True),
   Field('Number', unique=True),
   Field('Link','list:reference Link'),
   Field('GPS','list:reference GPS'),
   Field('GeoHash','list:reference GeoHash'),
   Field('OpenStreetMap','list:reference OpenStreetMap'),
   format = '%(Name)s')
   
db.define_table('Subway',
   Field('Name', unique=True),
   Field('Number', unique=True),
   format = '%(Name)s')
  

db.define_table('SubwayStation',
   Field('Name', unique=True),
   Field('Subway','list:reference Subway'),
   format = '%(Name)s')


db.define_table('Bus',
   Field('Name', unique=True),
   Field('Number', unique=True),
   format = '%(Name)s')
  

db.define_table('BusStation',
   Field('Name', unique=True),
   Field('Subway','list:reference Subway'),
   format = '%(Name)s')

db.define_table('Localisation',
   Field('Name', unique=True),
   Field('Link','list:reference Link'),
   Field('GPS','list:reference GPS'),
   Field('GeoHash','list:reference GeoHash'),
   Field('OpenStreetMap','list:reference OpenStreetMap'),
   Field('Country','list:reference Country'),
   Field('State','list:reference State'),
   Field('Region','list:reference Region'),
   Field('City','list:reference City'),
   Field('Adress','list:reference Adress'),
   Field('PostalCode','list:reference PostalCode'),
   Field('SubwayStation','list:reference SubwayStation'),
   Field('BusStation','list:reference BusStation'),
   format = '%(Name)s')
   

db.define_table('image',
   Field('title', unique=True),
   Field('file', 'upload'),
   format = '%(title)s')


db.define_table('Cour',
    Field('id'),
    Field('Price', 'double'),
    format = '%(Price)d')

db.define_table('Currency',
   Field('Name', unique=True),
   Field('Cour', db.Cour),
   format = '%(Name)s')
   
   
db.define_table('Price',
   Field('Name'),
   Field('Currency', db.Currency),
   Field('Amount', 'double'),
   format = '%(Price,Currency)s')
   
db.define_table('Seller',
   Field('Name', unique=True),
   Field('Date'),
   Field('Localisation','list:reference Localisation'),
   Field('Tag','list:reference Tag'),
   Field('Comment','list:reference Comment'),
   Field('Link','list:reference Link'),
   format = '%(Nom)s')   

db.define_table('FamilleTag',
   Field('Name', unique=True),
   Field('Tag','list:reference Tag'),
   format = '%(Name)s')
   
db.define_table('Tag',
   Field('Name', unique=True),
   format = '%(Name)s')
   
db.define_table('AssoTag',
   Field('Name', unique=True),
   Field('Tag','list:reference Tag'),
   Field('FamilleTag','list:reference FamilleTag'),
   format = '%(Name)s')
   
db.define_table('VoteHK',
   Field('auth_user', db.auth_user),
   format = '%(auth_user)s')
   
db.define_table('VoteNonHK',
   Field('auth_user', db.auth_user),
   format = '%(auth_user)s')

db.define_table('VoteAskHK',
   Field('auth_user', db.auth_user),
   format = '%(auth_user)s')

db.define_table('comment',
   Field('Barcode_id', db.Barcode),
   Field('author', db.auth_user),
   Field('body', 'text'))

## configure email
mail=auth.settings.mailer
mail.settings.server = 'logging' or 'smtp.gmail.com:587'
mail.settings.sender = 'you@gmail.com'
mail.settings.login = 'username:password'

## configure auth policy
auth.settings.registration_requires_verification = False
auth.settings.registration_requires_approval = False
auth.settings.reset_password_requires_verification = True

## if you need to use OpenID, Facebook, MySpace, Twitter, Linkedin, etc.
## register with janrain.com, write your domain:api_key in private/janrain.key
from gluon.contrib.login_methods.rpx_account import use_janrain
use_janrain(auth,filename='private/janrain.key')

#########################################################################
## Define your tables below (or better in another model file) for example
##
## >>> db.define_table('mytable',Field('myfield','string'))
##
## Fields can be 'string','text','password','integer','double','boolean'
##       'date','time','datetime','blob','upload', 'reference TABLENAME'
## There is an implicit 'id integer autoincrement' field
## Consult manual for more options, validators, etc.
##
## More API examples for controllers:
##
## >>> db.mytable.insert(myfield='value')
## >>> rows=db(db.mytable.myfield=='value').select(db.mytable.ALL)
## >>> for row in rows: print row.id, row.myfield
#########################################################################

#########