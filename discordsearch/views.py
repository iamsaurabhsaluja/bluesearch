from django.shortcuts import render
from discordsearch.models import Messages
from django.views.decorators.csrf import csrf_exempt

from discordsearch.services.ViewService import ViewService
from django.http import HttpResponse
import json, sys

def genericResponse( obj ):
    response = HttpResponse( json.dumps( obj ), content_type="application/json" )
    return response

def StatusResponse( status_info = None, status = None, data = None, updated_time = '' ):
    response = {}

    response['status_info'] = status_info;
    response['status'] = status;
    response['updated_time'] = str(updated_time);
    response['data'] = data

    return response;

@csrf_exempt
def startEngineView( request ):

    print("entered startEngineView")
    sys.stdout.flush()

    view_service = ViewService()
    view_service.startEngine()

    print("reached at response")
    sys.stdout.flush()

    response = StatusResponse(status_info = "Successful", status = '1001', data = {})

    return genericResponse( response )
