# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import LoginForm, SignUpForm
from employee_app.models import *
from handler_app.models import *
from admin_app.models import *
from django.contrib.auth.models import User, auth

def login_view(request):
    form = LoginForm(request.POST or None)
    msg = None
    if request.method == "POST":
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                employees = Employee.objects.filter(user = user)
                handlers = Handler.objects.filter(user = user)
                admins = Administrator.objects.filter(user = user)

                if len(employees) > 0:
                        login(request, user)
                        return redirect("informationmap")
                    
                elif len(handlers) > 0:
                        login(request, user)
                        return redirect("handlerReports")

                elif len(admins) > 0:
                        login(request, user)
                        return redirect("inforbuilding")     
            else:
                msg = 'Invalid credentials'
        else:
            msg = 'Error validating the form'

    return render(request, "accounts/login.html", {"form": form, "msg": msg})


def register_user(request):
    msg = None
    success = False

    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            raw_password = form.cleaned_data.get("password1")
            user = authenticate(username=username, password=raw_password)

            msg = 'User created - please <a href="/login">login</a>.'
            success = True

            # return redirect("/login/")

        else:
            msg = 'Form is not valid'
    else:
        form = SignUpForm()

    return render(request, "accounts/register.html", {"form": form, "msg": msg, "success": success})



def logoutUser(request):
    auth.logout(request)
    return redirect('login')