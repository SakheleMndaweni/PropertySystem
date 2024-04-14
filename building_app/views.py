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

from asgiref.sync import sync_to_async

# Building Api.

class BuildingApiView(APIView):
    
            parser_classes = (MultiPartParser,FormParser,JSONParser)
            permission_classes = (AllowAny,)
            """
            Building List and post
            """
            def post(self, request, format=None):
                    serializer = BuildingSerializer(data=request.data)
                    if serializer.is_valid():
                        serializer.save()
                        return Response(serializer.data, status=status.HTTP_201_CREATED)
                    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

            def get(self, request, format=None):
                    buildings = Building.objects.all()
                    serializer = BuildingSerializer(buildings, many=True)
                    return Response(serializer.data)

class Building_ApiView(APIView):
    """
    Retrieve, update or delete a product or item  instance.
    """
    parser_classes = (MultiPartParser,FormParser,JSONParser)
    permission_classes = (AllowAny,)
    def get_object(self, pk):
        try:
            return Building.objects.get(pk=pk)
        except Building.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        building = self.get_object(pk)
        serializer = BuildingSerializer(building)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        building = self.get_object(pk)
        serializer = BuildingSerializer(building, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse('building saved',safe=False)
        return JsonResponse('building Item data',safe=False)

    def delete(self, request, pk, format=None):
        building = self.get_object(pk)
        building.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# End Building Api

# Parking Api 

class ParkingApiView(APIView):
    
            parser_classes = (MultiPartParser,FormParser,JSONParser)
            permission_classes = (AllowAny,)
            """
            Building List and post
            """
            def post(self, request, format=None):
                    serializer = ParkingSerializer(data=request.data)
                    if serializer.is_valid():
                        serializer.save()
                        return Response(serializer.data, status=status.HTTP_201_CREATED)
                    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

            def get(self, request, format=None):
                    parking = Parking.objects.all()
                    serializer = ParkingSerializer(Parking, many=True)
                    return Response(serializer.data)

class Parking_ApiView(APIView):
    """
    Retrieve, update or delete a parking  instance.
    """
    parser_classes = (MultiPartParser,FormParser,JSONParser)
    permission_classes = (AllowAny,)
    def get_object(self, pk):
        try:
            return Parking.objects.get(pk=pk)
        except Parking.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        parking = self.get_object(pk)
        serializer = ParkingSerializer(parking)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        parking = self.get_object(pk)
        serializer = ParkingSerialize(parking, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse('building saved',safe=False)
        return JsonResponse('building Item data',safe=False)

    def delete(self, request, pk, format=None):
        parking = self.get_object(pk)
        parking.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

#End Parking Api 

#Boardroom Api
class BoardroomApiView(APIView):
    
            parser_classes = (MultiPartParser,FormParser,JSONParser)
            permission_classes = (AllowAny,)
            """
            Boardroom List and post
            """
            def post(self, request, format=None):
                    serializer = BoardroomSerializer(data=request.data)
                    if serializer.is_valid():
                        serializer.save()
                        return Response(serializer.data, status=status.HTTP_201_CREATED)
                    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

            def get(self, request, format=None):
                    boardroom = Boardroom.objects.all()
                    serializer = BoardroomSerializer(boardroom, many=True)
                    return Response(serializer.data)

class Boardroom_ApiView(APIView):
    """
    Retrieve, update or delete a Boardroom  instance.
    """
    parser_classes = (MultiPartParser,FormParser,JSONParser)
    permission_classes = (AllowAny,)
    def get_object(self, pk):
        try:
            return Boardroom.objects.get(pk=pk)
        except Boardroom.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        boardroom = self.get_object(pk)
        serializer = BoardroomSerializer(boardroom)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        boardroom = self.get_object(pk)
        serializer = BoardroomSerialize(boardroom, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse('building saved',safe=False)
        return JsonResponse('building Item data',safe=False)

    def delete(self, request, pk, format=None):
        boardroom = self.get_object(pk)
        boardroom.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

#End Boardroom Api

#Boardroom Booking Api
class BoardroomBookingApiView(APIView):
            parser_classes = (MultiPartParser,FormParser,JSONParser)
            permission_classes = (AllowAny,)
            """
            Boardroom List and post
            """
            def post(self, request, format=None):
                    serializer = BoardroomBookingSerializer(data=request.data)
                    if serializer.is_valid():
                        serializer.save()
                        return Response(serializer.data, status=status.HTTP_201_CREATED)
                    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

            def get(self, request, format=None):
                    boardroomBooking = BoardroomBooking.objects.all()
                    serializer = boardroomBookingSerializer(boardroom, many=True)
                    return Response(serializer.data)

class BoardroomBooking_ApiView(APIView):
    """
    Retrieve, update or delete a Boardroom  instance.
    """
    parser_classes = (MultiPartParser,FormParser,JSONParser)
    permission_classes = (AllowAny,)
    def get_object(self, pk):
        try:
            return BoardroomBooking.objects.get(pk=pk)
        except BoardroomBooking.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        boardroomBooking = self.get_object(pk)
        serializer = BoardroomBookingSerializer(boardroomBooking)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        boardroomBooking = self.get_object(pk)
        serializer = BoardroomBookingSerialize(boardroomBooking, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse('building saved',safe=False)
        return JsonResponse('building Item data',safe=False)

    def delete(self, request, pk, format=None):
        boardroomBooking = self.get_object(pk)
        boardroomBooking.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# end Boardroom booking 

# Parking Booking 
class ParkingBookingApiView(APIView):
    
            parser_classes = (MultiPartParser,FormParser,JSONParser)
            permission_classes = (AllowAny,)
            """
            Boardroom List and post
            """
            def post(self, request, format=None):
                    serializer = ParkingBookingSerializer(data=request.data)
                    if serializer.is_valid():
                        serializer.save()
                        return Response(serializer.data, status=status.HTTP_201_CREATED)
                    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

            def get(self, request, format=None):
                    parkingBooking = ParkingBooking.objects.all()
                    serializer = ParkingBookingSerializer(parkingBooking, many=True)
                    return Response(serializer.data)


class ParkingBooking_ApiView(APIView):
    """
    Retrieve, update or delete a Boardroom  instance.
    """
    parser_classes = (MultiPartParser,FormParser,JSONParser)
    permission_classes = (AllowAny,)
    def get_object(self, pk):
        try:
            return ParkingBooking.objects.get(pk=pk)
        except ParkingBooking.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        parkingBooking = self.get_object(pk)
        serializer = ParkingBookingSerializer(parkingBooking)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        parkingBooking = self.get_object(pk)
        serializer = ParkingBookingSerialize(parkingBooking, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse('ParkingBooking saved',safe=False)
        return JsonResponse('ParkingBooking Item data',safe=False)

    def delete(self, request, pk, format=None):
        parkingBooking = self.get_object(pk)
        parkingBooking.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

#End Parking Booking


