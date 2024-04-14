from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from building_app.views import *

urlpatterns = [
    path('building/', BuildingApiView().as_view()),
    path('building/<int:pk>/', Building_ApiView.as_view()),
    #parking 
    path('parking/', ParkingApiView().as_view()),
    path('parking/<int:pk>/', Parking_ApiView.as_view()),
    #Parking Booking
    path('parking/booking/', ParkingBookingApiView().as_view()),
    path('parking/booking/<int:pk>/', Parking_ApiView.as_view()),
    #boardroom 
    path('boardroom/', BoardroomApiView().as_view()),
    path('boardroom/<int:pk>/', Boardroom_ApiView.as_view()),
    #boardroom booking
    path('booking/boardroom/', BoardroomBookingApiView().as_view()),
    path('booking/boardroom/<int:pk>/', BoardroomBooking_ApiView.as_view()),
    

]

urlpatterns = format_suffix_patterns(urlpatterns)