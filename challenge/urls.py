from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'challenge.views.home', name='home'),
    url(r'^polygon/', include('polygonapp.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
