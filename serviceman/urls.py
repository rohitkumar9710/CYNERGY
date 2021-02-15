
from django.urls import path
from . import views
urlpatterns = [
    path("",views.redirect,name = "redirect"),
    path("otp",views.otp,name = "otp"),
    path("otp/status",views.status,name = "status"),
    path("login",views.login,name= "login"),
    path("login/loggedin",views.profile_serviceman,name = "serviceman_home"),
    path("login/loggedin/services",views.services,name = "services"),
    path("login/loggedin/services/update",views.servicelist_update,name = "services_update"),
    path("login/loggedin/aboutus",views.aboutus,name = "aboutus"),
    path("login/loggedin/logout",views.logout,name = "logout"),
    path("login/loggedin/contactus",views.contactus,name = "contactus"),
    path("login/loggedin/contactus/contact_status",views.contact_submit,name = "contact_submit"),
]