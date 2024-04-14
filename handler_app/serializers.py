from django.db.models import fields
from rest_framework import serializers
from .models import *

class HandlerSerializer(serializers.ModelSerializer):
        class Meta:
            model = Handler
            fields = ('name','surname','phone','email','address','zipCode','employeeNumber')