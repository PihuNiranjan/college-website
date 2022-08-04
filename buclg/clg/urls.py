# from django.contrib import admin
from django.urls import path
# from django.views import View
from . import views

urlpatterns = [
    path("",views.loginuser,name="loginuser"),
    path("home",views.home,name="home"),
    path("about",views.about,name="about"),
    path("profile",views.profile,name="profile"),
    path("newstudent",views.newstudent,name="newstudent"),
    path("strec",views.strec,name="strec"),
    path("loginuser",views.loginuser,name="loginuser"),
    path("logoutuser",views.logoutuser,name="logoutuser"),
    path("register",views.register,name="register"),
    path("attendance",views.attendance,name="attendance"),
    path("fees",views.fees,name="fees"),
    path("attenddata",views.attenddata,name="attenddata"),

]
