from django.urls import path
from .views import login_view, register_user,logoutUser
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('', login_view, name="login"),
    path('register/', register_user, name="register"),
    path('logout/', logoutUser , name='logout'),
]
