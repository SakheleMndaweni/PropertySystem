from django.contrib.auth.models import User, auth
from django.shortcuts import render , redirect
from admin_app.models import *
from building_app.models import *
from employee_app import *
from handler_app import *
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import Http404

def get_administrator_object(user):
        try:
            return Administrator.objects.get(user = user)
        except Administrator.DoesNotExist:
            raise Http404


@login_required(login_url='login')
def administrator_home(request):
        context ={}
        return render(request, "administrator/administrator.html",context)

def administrator_building_view(request):
        admin = get_administrator_object(request.user)
        buildings = Building.objects.all()
        context ={'buildings':buildings,'admin':admin}
        
        return render(request, "administrator/buildings.html",context)

def administrator_building_update_view(request,pk):
        admin = get_administrator_object(request.user)
        building = Building.objects.get(id = pk)
        context  ={'building': building,'admin':admin}
        return render(request, "administrator/building_update.html",context)


def administrator_employee_view(request):
        admin = get_administrator_object(request.user)
        employees = Employee.objects.all()
        context ={'employees':employees,'admin':admin}
        
        return render(request, "administrator/employees.html",context)

def administrator_employee_update_view(request,pk):
        admin = get_administrator_object(request.user)
        employee = Employee.objects.get(id = pk)
        context  ={'employee': employee ,'admin':admin}
        return render(request, "administrator/employee_update.html",context)

def administrator_handler_view(request):
        admin = get_administrator_object(request.user)
        handlers = Handler.objects.all()
        context ={'handlers':handlers ,'admin':admin}
        return render(request, "administrator/handlers.html",context)

def administrator_handler_update_view(request,pk):
        admin = get_administrator_object(request.user)
        handler = Handler.objects.get(id = pk)
        context  ={'handler': handler ,'admin':admin}
        return render(request, "administrator/handlers_update.html",context)


def administrator_reports_view(request):
        admin = get_administrator_object(request.user)
        selection_buildings = Building.objects.all()
        context ={'buildings':selection_buildings,'admin':admin}
        return render(request, "administrator/reports.html",context)

def administrator_building_reports_view(request,pk):
        admin = get_administrator_object(request.user)
        building = Building.objects.get(id = pk)
        reports  = Report.objects.filter(building = building)
        context ={'reports':reports,'admin':admin}
        return render(request, "administrator/reports_information.html",context)


def administrator_parking_bookings_view(request):
        admin = get_administrator_object(request.user)
        buildings = Building.objects.all()
        context ={'buildings':buildings,'admin':admin}
        return render(request, "administrator/parking_booking.html",context)

def administrator_parking_selection_bookings_view(request,pk):
        admin = get_administrator_object(request.user)
        building =  Building.objects.get(id = pk)
        parkings =  ParkingBooking.objects.filter(building = building)
        context ={'parkings':parkings,'admin':admin}
        return render(request, "administrator/parking_booking_information.html",context)

def administrator_boardroom_bookings_view(request):
        admin = get_administrator_object(request.user)
        buildings = Building.objects.all()
        context ={'buildings':buildings,'admin':admin}
        return render(request, "administrator/boardroom_booking.html",context)

def administrator_boardroom_selection_bookings_view(request,pk):
        admin = get_administrator_object(request.user)
        building =  Building.objects.get(id = pk)
        parkings =  BoardroomBooking.objects.filter(building = building)
        context ={'parkings':parkings,'admin':admin}
        return render(request, "administrator/boardroomg_booking_information.html",context)

