#!/usr/bin/python
#coding=utf-8
from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
import view

admin.autodiscover()

urlpatterns = patterns('',
                       # Examples:
                       # url(r'^$', 'djangowebbuild.views.home', name='home'),
                       # url(r'^djangowebbuild/', include('djangowebbuild.foo.urls')),

                       # Uncomment the admin/doc line below to enable admin documentation:

                       url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

                       # Uncomment the next line to enable the admin:

                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^mail/$', view.mail),
                       url(r'^tieba/', view.tiebaform),

                       url(r'^search/', view.search),


                       #默认页面导向r''必须放在最后去匹配
                       url(r'', view.tiebaform),
                       )
