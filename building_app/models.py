from django.db import models
from handler_app.models import *
from employee_app.models import *

class Building(models.Model):
        name = models.CharField(max_length=200, null=True)
        address = models.CharField(max_length=200, null=True)
        zipCode = models.CharField(max_length=200, null=True)
        city = models.CharField(max_length=200, null=True)
        def __str__(self):
            return self.name

def random_id(length):
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    id = ''
    for i in range(0,length,2):
        id += random.choice(alpha)
    return id

def default_function():
    return  random_id(10)

class Parking(models.Model):
        parking_id =  models.CharField(
                            max_length = 14,
                            blank=True,
                            editable=False,
                            default= default_function
                            )
        building = models.ForeignKey(Building, on_delete=models.SET_NULL, null=True, blank=True)
        address = models.CharField(max_length=200, null=True)
        zipCode = models.CharField(max_length=200, null=True)
        province = models.CharField(max_length=200, null=True)
        def __str__(self):
            return self.parking_id

class Boardroom(models.Model):
        boardroom_id =  models.CharField(
                            max_length = 14,
                            blank=True,
                            editable=False,
                            default= default_function
                            )
        building = models.ForeignKey(Building, on_delete=models.SET_NULL, null=True, blank=True)
        capacity = models.IntegerField()
        address  = models.CharField(max_length=200, null=True)
        zipCode  = models.CharField(max_length=200, null=True)
        province = models.CharField(max_length=200, null=True)
        def __str__(self):
            return self.boardroom_id 

class Report(models.Model):
        report_id =  models.CharField(
                            max_length = 14,
                            blank=True,
                            editable=False,
                            default= default_function
                            )
        building         = models.ForeignKey(Building, on_delete=models.SET_NULL, null=True, blank=True)
        reporter         = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True, blank=True)
        handler          = models.ForeignKey(Handler, on_delete=models.SET_NULL, null=True, blank=True)
        description      = models.TextField()
        reportedDate     = models.CharField(max_length=200, null=True)
        handledDate      = models.CharField(max_length=200, null=True)
        handlerSolution  = models.TextField()

        def __str__(self):
            return self.boardroom_id


class ParkingBooking(models.Model):
        booking_id =  models.CharField(
                            max_length = 14,
                            blank=True,
                            editable=False,
                            default= default_function
                            )
        
        building     = models.ForeignKey(Building, on_delete=models.SET_NULL, null=True, blank=True)
        creator      = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True, blank=True)
        description  = models.TextField()
        startDate    = models.DateTimeField(max_length=200, null=True)
        endDate      = models.DateTimeField(max_length=200, null=True)
        def __str__(self):
            return self.booking_id

class ParkingBookingItem(models.Model):
        parking = models.ForeignKey(Parking, on_delete=models.SET_NULL, null=True, blank=True)
        handler = models.ForeignKey(ParkingBooking, on_delete=models.SET_NULL, null=True, blank=True)
        

class BoardroomBooking(models.Model):
        boardroom_booking_id =  models.CharField(
                            max_length = 14,
                            blank=True,
                            editable=False,
                            default= default_function
                            )
        
        building     = models.ForeignKey(Building, on_delete=models.SET_NULL, null=True, blank=True)
        creator      = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True, blank=True)
        description  = models.TextField()
        startDate    = models.CharField(max_length=200, null=True)
        endDate      = models.CharField(max_length=200, null=True)
        def __str__(self):
            return self.boardroom_booking_id

class BoardroomBookingItem(models.Model):
        boadroom = models.ForeignKey(Parking, on_delete=models.SET_NULL, null=True, blank=True)
        handler = models.ForeignKey(BoardroomBooking, on_delete=models.SET_NULL, null=True, blank=True)