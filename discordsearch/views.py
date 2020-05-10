from django.shortcuts import render
from discordsearch.models import Messages
from django.views.decorators.csrf import csrf_exempt

from discordsearch.services.ViewService import ViewService

# Create your views here.

@csrf_exempt
def startEngineView( request ):
    view_service = ViewService()
    view_service.startEngine()
