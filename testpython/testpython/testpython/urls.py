from django.conf.urls import patterns, include, url
from django.contrib import admin
from testpython.view.hello import home, car, template, say
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^(\d+)$', car, name='car'),
    url(r'^home/$', home, name='home'),
    url(r'^template/$', template, name='template'),
    url(r'^say/$', say, name='say'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls))
)
