from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('siteYoda.core.views',
    url(r'^$', 'home', name='home'),
    url(r'^cadastrar/$', 'cadastrar', name='cadastrar'),
    url(r'^admin/', include(admin.site.urls)),
)
