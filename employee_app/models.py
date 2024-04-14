from django.db import models
from django.contrib.auth.models import User

class Employee(models.Model):
        user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
        name = models.CharField(max_length=200, null=True)
        surname = models.CharField(max_length=200, null=True)
        phone = models.CharField(max_length=200, null=True)
        email = models.CharField(max_length=200)
        address = models.CharField(max_length=200, null=True)
        zipCode = models.CharField(max_length=200, null=True)
        employeeNumber = models.CharField(max_length=200, null=True)
        def __str__(self):
            return self.name