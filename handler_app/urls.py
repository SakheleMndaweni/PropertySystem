from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from handler_app.views import *

urlpatterns = [
    path('report/handler/', HandlerApiView().as_view()),
    path('report/handler/<int:pk>/', Handler_ApiView.as_view()),

    path('handler/buildings/',handler_reports_view ,name='handlerReports'),
    path('handler/building/reports/<int:pk>/',  handler_reports_information_view ,name='handlerreportsinformation'),
    path('handler/profile/', handler_profile,name='handlerprofile'),
    path('user/handler/notification/', handler_notification,name='notificationhandler'),
]

urlpatterns = format_suffix_patterns(urlpatterns)