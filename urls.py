from django.contrib import admin
from django.conf.urls.defaults import patterns, include, url
admin.autodiscover()

urlpatterns = patterns('',
    # # Examples:
    url(r'^$', 'xserver.views.index', name='home'),

    url(r'additem', 'xserver.views.additem', name='additem'),

    # # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
