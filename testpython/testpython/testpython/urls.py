from django.conf.urls import patterns, include, url
from django.contrib import admin
from testpython.view.hello import home, car, say, settings
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^(\d+)$', car, name='car'),
    url(r'^$', home, name='home'),
    url(r'^say/$', say, name='say'),
    url(r'^settings/', settings)
)
