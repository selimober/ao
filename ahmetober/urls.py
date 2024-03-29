from django.conf.urls.defaults import patterns, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from ahmetober.views import IndexView, ContactView, SorularView, CVView, TodoView, SEOView, RobotView
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
    url(r'^sorular$', SorularView.as_view()),
    url(r'^cv$', CVView.as_view()),
    url(r'^iletisim', ContactView.as_view()),
    url(r'^todo$', TodoView.as_view()),
    url(r'^konular/?(.*)', 'ahmetober.views.article'),
    url(r'^sitemap\.xml$', SEOView.as_view()),
    url(r'^robots\.txt$', RobotView.as_view()),
)

urlpatterns += staticfiles_urlpatterns()
#if DEBUG:
#
#    urlpatterns += patterns('', (
#        r'^static/(?P<path>.*)$',
#        'django.views.static.serve',
#        {'document_root': 'static'}
#    ))
