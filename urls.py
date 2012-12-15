from django.conf.urls.defaults import patterns, include

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()
from django.http import HttpResponseRedirect

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ao.views.home', name='home'),
    # url(r'^ao/', include('ao.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    (r'^ahmetober/', include('ahmetober.urls')),
)
