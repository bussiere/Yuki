from settings import INSTALLED_APPS
import os

for app in INSTALLED_APPS:
	print app
	os.system('python manage.py convert_to_south %s' % app)
