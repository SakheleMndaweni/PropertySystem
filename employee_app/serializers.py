from django.db.models import fields
from rest_framework import serializers
from .models import *

class EmployeeSerializer(serializers.ModelSerializer):
        class Meta:
            model = Employee
            fields = ('name','surname','phone','email','address','zipCode','employeeNumber')