
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^startEngine$', views.startEngineView, name='startEngine'),
]

#from discordsearch.services import initiateEngine
