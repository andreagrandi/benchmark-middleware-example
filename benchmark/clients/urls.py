from django.conf.urls import patterns, include, url
from clients import views


urlpatterns = patterns(
    '',
    url(r'^$', views.ListClientView.as_view(), name='clients-list', ),
)
