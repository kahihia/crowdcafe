from django.conf.urls import patterns, include, url

import views

urlpatterns = patterns('',
    #===============================================================================
    # Views
    #-------------------------------------------------------------------------------
    url(r'auth/$', views.Auth, name='cafe-auth'),  
    url(r'welcome/$', views.Welcome, name='cafe-home'),
)
