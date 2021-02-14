
from django.urls import path
from . import views
urlpatterns = [
    path("",views.redirect,name = "redirect"),
    path("otp",views.otp,name = "otp"),
    path("otp/status",views.status,name = "status"),
    path("login",views.login,name= "login"),
    path("login/profile_serviceman",views.profile_serviceman,name = "Serviceman_home")
]