# from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from .models import Web3event
from .models import EventUrl
from .serializers import EventUrlSerializer
from django.http import HttpResponse
from django.core import serializers
import json

def get_all_events(request):
    """
    Lis all web3 events or create a new event
    """

    if request.method == 'GET':
        events = EventUrl.objects.all()
        serializers = EventUrlSerializer(events, many = True)

        return HttpResponse("Hello, world!")
    else:
        return HttpResponse("get all error")
    
def create_event(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        time = request.POST.get('time')
        image = request.POST.get('image')
        address = request.POST.get('address')
        organizers = request.POST.get('organizers')
        presenter = request.POST.get('presenter')
        tags = request.POST.get('tags')

        Web3event.objects.create(title=title,time=time,image=image,address=address,organizers=organizers,presenter=presenter,tags=tags,description=description)
        
        return HttpResponse("create successfully")
    else :
        return HttpResponse("create error")

        # Web3event.objects.create(title='hello', image='')

        # serializer = Web3eventSerializer(data = request.data)
        # if serializer.is_valid():
        #     serializer.save()
        #     return Response(serializer.data,
        #                     status = status.HTTP_201_CREATED)
        # return Response(serializer.errors,
        #                 status = status.HTTP_400_BAD_REQUEST)

def create_event_url(request):
    if request.method == 'POST':
        source_url = request.POST.get('source_url')
        EventUrl.objects.create(source_url=source_url, type='')
        return HttpResponse("create successfully")
    else :
        return HttpResponse("create error")

        # Web3event.objects.create(title='hello', image='')

        # serializer = Web3eventSerializer(data = request.data)
        # if serializer.is_valid():
        #     serializer.save()
        #     return Response(serializer.data,
        #                     status = status.HTTP_201_CREATED)
        # return Response(serializer.errors,
        #                 status = status.HTTP_400_BAD_REQUEST)
    



