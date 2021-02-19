
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
    
    path("login/loggedin/services/search",views.search,name = "services_search"),
    path("login/loggedin/services/search/request",views.search_request,name = "services_search_request"),
    path("login/loggedin/services/search/random_data",views.random_data,name = "services_random_data"),
    path("login/loggedin/notification",views.notification,name = "notification"),  
    path("login/loggedin/notification/feedback",views.feedback,name = "feedback"),  
    path("login/loggedin/notification/cencle_button",views.cencle_button,name = "cencle_button"),  
    path("login/loggedin/history",views.history,name = "history"),  
    path("login/loggedin/donate",views.donate,name = "donate"),  
    path("login/loggedin/contact",views.contact,name = "contact"),  
    path("login/loggedin/contact/contact_status",views.contact_submit,name = "contact_submit"),  
    path("login/loggedin/logout",views.logout,name = "logout"),  
    path("login/loggedin/profile/profileupdate",views.profileupdate,name = "profileupdate"),  
]
