from django.shortcuts import render
from .serializers import *
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
from rest_framework.permissions import AllowAny
from django.shortcuts import render
import json
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser
from django.views.decorators.csrf import csrf_exempt
import time
import aiohttp
import asyncio
from asgiref.sync import sync_to_async
from building_app.models import *

def get_handler_object(user):
        try:
            return Handler.objects.get(user = user)
        except Handler.DoesNotExist:
            raise Http404


def handler_reports_view(request):
        handler = get_handler_object(request.user)
        buildings =Building.objects.all()
        context ={'segment':'reports','buildings':buildings,'handler':handler}
        return render(request, "handler/handler.html",context)

def handler_reports_information_view(request,pk):
        handler = get_handler_object(request.user)
        building =Building.objects.get(id = pk)
        reports =  Report.objects.filter(building = building)
        context ={'segment':'reports','repors':building,'handler':handler}
        return render(request, "handler/report_handling.html",context)

def handler_profile(request):
        handler = get_handler_object(request.user)
        context ={'segment':'profile','handler':handler}
        return render(request, "handler/user_profile.html",context)

def handler_notification(request):
        handler = get_handler_object(request.user)
        context ={'segment':'notifications','handler':handler}
        return render(request, "handler/notification.html",context)

class HandlerApiView(APIView):
            parser_classes = (MultiPartParser,FormParser,JSONParser)
            permission_classes = (AllowAny,)
            """
            Handler List and post
            """
            def post(self, request, format=None):
                    serializer = HandlerSerializer(data=request.data)
                    if serializer.is_valid():
                        serializer.save()
                        return Response(serializer.data, status=status.HTTP_201_CREATED)
                    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

            def get(self, request, format=None):
                    handlers = Handler.objects.all()
                    serializer = HandlerSerializer(handlers, many=True)
                    return Response(serializer.data)

class Handler_ApiView(APIView):
    """
    Retrieve, update or delete a Handler  instance.
    """
    parser_classes = (MultiPartParser,FormParser,JSONParser)
    permission_classes = (AllowAny,)
    def get_object(self, pk):
        try:
            return Handler.objects.get(pk=pk)
        except Handler.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        handler = self.get_object(pk)
        serializer = HandlerSerializer(handler)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        handler = self.get_object(pk)
        serializer = HandlerSerializer(handler, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse('Handler saved',safe=False)
        return JsonResponse('Handler Item data',safe=False)

    def delete(self, request, pk, format=None):
        handler = self.get_object(pk)
        handler.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
