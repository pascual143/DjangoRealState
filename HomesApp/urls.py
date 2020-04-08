from django.conf.urls import include, url
from django.contrib import admin
from .import views

urlpatterns = [
        #/HomesApp/
        url(r'^$', views.IndexView.as_view(), name='index'),
        #/HomesApp/1
        url(r'^(?P<pk>[0-9]+)/$', views.LocationView.as_view(),name='property'),
        #/HomesApp/1/2
        url(r'^([0-9]+)/(?P<pk>[0-9]+)/$', views.PropertyDetail.as_view(), name='propertyview'),
    ]