from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from admin_app.views import *

urlpatterns = [
    path('administrator/home/', administrator_home,name='home' ),
    path('administrator/buildings/', administrator_building_view, name='inforbuilding'),
    path('administrator/building/update/<int:pk>/', administrator_building_update_view ,name ='updateBuilding'),

    path('administrator/employees/', administrator_employee_view, name='employeesInformation'),
    path('administrator/employee/update/<int:pk>/', administrator_employee_update_view ,name ='update_employee'),

    path('administrator/handlers/', administrator_handler_view, name='report_handler'),
    path('administrator/handler/update/<int:pk>/', administrator_handler_update_view ,name ='update_system_handler'),

    path('administrator/boardrooms/', administrator_boardroom_bookings_view, name='bookingBoardrooms'),
    path('administrator/bookings/boardroom/<int:pk>/', administrator_boardroom_selection_bookings_view ,name ='boardrooms_Booking'),

    path('administrator/parkings/', administrator_parking_bookings_view, name='parkingBooking'),
    path('administrator/bookings/parkings/<int:pk>/', administrator_parking_selection_bookings_view ,name ='parking_booking_infor'),

    path('administrator/reports/', administrator_reports_view, name='report_selection'),
    path('administrator/reports/informatio/<int:pk>/',administrator_building_reports_view ,name ='allreporta'),

    
]

urlpatterns = format_suffix_patterns(urlpatterns)