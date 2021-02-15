
from django.urls import path
from . import views
urlpatterns = [
    path("",views.redirect,name = "redirect"),
    path("otp",views.otp,name = "otp"),
    path("otp/status",views.status,name = "status"),
    path("login",views.login,name= "login"),
    path("login/loggedin",views.profile_customer,name = "customer_home"),
    path("login/loggedin/about",views.about,name = "about"),
    path("login/loggedin/profile",views.profile,name = "profile"),
    path("login/loggedin/services",views.services,name = "services"),  
    path("login/loggedin/contact",views.contact,name = "contact"),  
    path("login/loggedin/contact/contact_status",views.contact_submit,name = "contact_submit"),  
    path("login/loggedin/logout",views.logout,name = "logout"),  
    path("login/loggedin/profile/profileupdate",views.profileupdate,name = "profileupdate"),  
]
