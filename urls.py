from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'project.views.home', name='home'),
    url(r'^catalog/', include('catalog.urls')),
    url(r'^admin/', include(admin.site.urls)),
    # ex: /login/
    url(r'^login/$', 'project.views.login', name='login'),
)
