from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('FormGen.views',
    # Examples:
    url(r'^$', 'home', name='home'),
    url(r'^insert/$', 'update', name='update'),
    url(r'^print/$', 'examination_form', name='form')
)
