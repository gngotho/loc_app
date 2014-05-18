from django.conf.urls import url, patterns

urlpatterns = patterns('polygonapp.views',
    url(r'^$', 'index', name='index'),
    url(r'^show_polygon/$', 'region', name='showmap'),
    )