from django.conf.urls import patterns, include, url
from pubmed import views

urlpatterns = patterns('',
    url(r'^', views.dispatch),
)
