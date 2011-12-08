from django.conf.urls.defaults import patterns, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()
from ahmetober.views import IndexView, ContactView, SSSView, ArticlesView, CVView
from settings import DEBUG

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ao.views.home', name='home'),
    # url(r'^ao/', include('ao.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    url(r'^$', IndexView.as_view()),
    url(r'^articles$', ArticlesView.as_view()),
    url(r'^sss$', SSSView.as_view()),
    url(r'^cv$', CVView.as_view()),
    url(r'^contact$', ContactView.as_view()),
    url(r'^articles/(.*)', 'ahmetober.views.article'),
)

if DEBUG:
    urlpatterns += patterns('', (
        r'^static/(?P<path>.*)$',
        'django.views.static.serve',
        {'document_root': 'static'}
    ))