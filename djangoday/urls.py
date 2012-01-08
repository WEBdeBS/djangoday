from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()
from main.views import CallForPaperView, ThanksView

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'djangoday.main.views.home', name='home'),

    # url(r'^djangoday/', include('djangoday.foo.urls')),
    url(r'^subscribe/$','djangoday.main.views.subscribe', name='subscribe'),
    url(r'^cfp/$',CallForPaperView.as_view(), name='cfp'),
    url(r'^thanks/$',ThanksView.as_view(), name='thanks'),


    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
