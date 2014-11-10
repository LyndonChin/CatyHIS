from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'CatyHIS.views.home', name='home'),
    url(r'^form/', include('FormGen.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
