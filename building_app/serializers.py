from django.db.models import fields
from rest_framework import serializers
from .models import *

class BuildingSerializer(serializers.ModelSerializer):
        class Meta:
            model = Building
            fields = ('name','address', 'zipCode','city')

class ParkingSerializer(serializers.ModelSerializer):
        class Meta:
            model = Parking
            fields = ('building', 'address', 'zipCode','province')

class ParkingBookingSerializer(serializers.ModelSerializer):
        class Meta:
            model = ParkingBooking
            fields = ('building','creator','description','startDate','endDate')

class BoardroomSerializer(serializers.ModelSerializer):
        class Meta:
            model = Boardroom
            fields = ('building','capacity','address','zipCode','province')

class BoardroomBookingSerializer(serializers.ModelSerializer):
        class Meta:
            model = BoardroomBooking
            fields = ('building','creator','description','startDate','endDate')

class ReportSerializer(serializers.ModelSerializer):
        class Meta:
            model = Report
            fields = ('building','reporter','handler','description','reportedDate','handledDate','handlerSolution')