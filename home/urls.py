
from django.urls import path, re_path
from home import views

urlpatterns = [

    # The home page

    # Matches any html file
    re_path(r'^.*\.*', views.pages, name='pages'),

]