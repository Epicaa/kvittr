from django.conf.urls import patterns, url
from birds import views

urlpatterns = patterns('',
    url(r'^login$', views.bird_login, name='bird_login'),
    url(r'^logout$', views.bird_logout, name='bird_logout'),
    url(r'^register$', views.bird_register, name='bird_register'),
)