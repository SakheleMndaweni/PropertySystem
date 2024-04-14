from django.shortcuts import render
from django.contrib.auth.models import User, auth
from django.shortcuts import render , redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
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
from .serializers import *
from building_app.models import *
from handler_app.models import *

def get_employee_object(user):
        try:
            return Employee.objects.get(user = user)
        except Employee.DoesNotExist:
            raise Http404

@login_required(login_url='login')
def employee_home(request):
        context ={}
        return render(request, "employee/administrator.html",context)

def employee_building_view(request):
        employee = get_employee_object(request.user)
        buildings = Building.objects.all()
        context ={'segment':'buildings','buildings':buildings,'employee':employee}
        return render(request, "employee/buildings.html",context)

def employee_map_building_view(request,pk):
        employee = get_employee_object(request.user)
        building =Building.objects.get(id = pk)
        context ={'segment':'buildings','building':building,'employee':employee}
        return render(request, "employee/buildings_direction.html",context)

def employee_parkings_view(request):
        employee = get_employee_object(request.user)
        buildings = Building.objects.all()
        context ={'segment':'parking','buildings':buildings,'employee':employee}
        return render(request, "employee/parking.html",context)

def employee_book_parkings_view(request,pk):
        employee = get_employee_object(request.user)
        building =Building.objects.get(id = pk)
        parkings =  Parking.objects.filter(building = building)
        context ={'segment':'parking','parkings':parkings,'building':building,'employee':employee}
        return render(request, "employee/parking_information.html",context)

def employee_boardrooms_view(request):
        employee = get_employee_object(request.user)
        buildings =Building.objects.all()
        context ={'segment':'boardroom','buildings':buildings,'employee':employee}
        return render(request, "employee/boardroom.html",context)

def employee_book_boardrooms_view(request,pk):
        employee = get_employee_object(request.user)
        building =Building.objects.get(id = pk)
        boardrooms =  Boardroom.objects.filter(building = building)
        context ={'segment':'boardroom','boardrooms':building,'employee':employee}
        return render(request, "employee/boardroom_information.html",context)


def employee_reports_view(request):
        employee = get_employee_object(request.user)
        buildings =Building.objects.all()
        context ={'segment':'report','buildings':buildings,'employee':employee}
        return render(request, "employee/reports.html",context)

def employee_reports_information_view(request,pk):
        employee = get_employee_object(request.user)
        building =Building.objects.get(id = pk)
        reports =  Report.objects.filter(building = building)
        context ={'segment':'report','repors':building,'employee':employee}
        return render(request, "employee/reports_information.html",context)

def employee_profile(request):
        employee = get_employee_object(request.user)
        context ={'segment':'page-user','employee':employee}
        return render(request, "employee/user_profile.html",context)

def employee_notification(request):
        employee = get_employee_object(request.user)
        context ={'segment':'notification','employee':employee}
        return render(request, "employee/notification.html",context)

def employee_leaseviewFunction(request):
        employee = get_employee_object(request.user)
        buildings = Building.objects.all()
        context ={'segment':'lease','employee':employee,'buildings':buildings}
        return render(request, "employee/lease.html",context)

def employee_projects(request):
        employee = get_employee_object(request.user)
        context ={'segment':'projects','employee':employee}
        return render(request, "employee/projects.html",context)

def employee_reporting(request):
        employee = get_employee_object(request.user)
        context ={'segment':'reporting','employee':employee}
        return render(request, "employee/reporting.html",context)

def employee_municipal(request):
        employee = get_employee_object(request.user)
        context ={'segment':'municipal','employee':employee}
        return render(request, "employee/municipal.html",context)


def employee_court(request):
        employee = get_employee_object(request.user)
        context ={'segment':'court','employee':employee}
        return render(request, "employee/court.html",context)

def employee_renovations(request):
        employee = get_employee_object(request.user)
        context ={'segment':'renovations','employee':employee}
        return render(request, "employee/renovations.html",context)

def employee_projectbudget(request):
        employee = get_employee_object(request.user)
        context ={'segment':'budget','employee':employee}
        return render(request, "employee/projectbudget.html",context)

def employee_systempeporting(request):
        employee = get_employee_object(request.user)
        context ={'segment':'report','employee':employee}
        return render(request, "employee/systempeporting.html",context)

def employee_newbuilding(request):
        employee = get_employee_object(request.user)
        context ={'segment':'newbuilding','employee':employee}
        return render(request, "employee/newbuilding.html",context)

def employee_aump(request):
        employee = get_employee_object(request.user)
        context ={'segment':'aump','employee':employee}
        return render(request, "employee/aump.html",context)

class EmployeeApiView(APIView):
    
            parser_classes = (MultiPartParser,FormParser,JSONParser)
            permission_classes = (AllowAny,)
            """
            Employee List and post
            """
            def post(self, request, format=None):
                    serializer = EmployeeSerializer(data=request.data)
                    if serializer.is_valid():
                        serializer.save()
                        return Response(serializer.data, status=status.HTTP_201_CREATED)
                    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

            def get(self, request, format=None):
                    employees = Employee.objects.all()
                    serializer = EmployeeSerializer(employees, many=True)
                    return Response(serializer.data)

class Employee_ApiView(APIView):
    """
    Retrieve, update or delete a Employee  instance.
    """
    parser_classes = (MultiPartParser,FormParser,JSONParser)
    permission_classes = (AllowAny,)
    def get_object(self, pk):
        try:
            return Employee.objects.get(pk=pk)
        except Employee.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        employee = self.get_object(pk)
        serializer = EmployeeSerializer(employee)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        employee = self.get_object(pk)
        serializer = EmployeeSerializer(employee, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse('building saved',safe=False)
        return JsonResponse('building Item data',safe=False)

    def delete(self, request, pk, format=None):
        employee = self.get_object(pk)
        employee.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
