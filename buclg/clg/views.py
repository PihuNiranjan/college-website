from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from datetime import datetime
from clg.models import Attendance


# Create your views here.

def home(req):
    if req.user.is_anonymous:
        return redirect("/login")
    return render(req,"home.html")
    
def newstudent(req):
    return render(req,"register.html")

def about(req):
    return render(req,"about.html")

def strec(req):
    return render(req,"strec.html")

def loginuser(req):
    if req.method == "POST":
        username = req.POST.get("username")
        password = req.POST.get("password")
        # print(username , password)
        user = authenticate(username=username,password=password)

        if user is not None:
            login(req, user)
            return redirect("/home")
        else:
            return render(req,"login.html")
    return render(req,"login.html")

def logoutuser(req):
    logout(req)
    return render(req,"login.html")

def register(req):
    if req.method=="POST":
        username = req.POST['username']
        f_name = req.POST['fname']
        l_name = req.POST['lname']
        
        email = req.POST['email']
        password = req.POST['password']
        # cpassword = req.POST['password2']
        
        
        user = User.objects.create_user(username ,email ,password)
        
        user.first_name = f_name.capitalize() 
        user.last_name = l_name.capitalize()
        user.save()
        

        

        return redirect("/loginuser")


    return render(req,"register.html")
        
def profile(req):
    
    return render(req,"profile.html")

def attendance(req):
    return render(req,"attendance.html")

def attenddata(req):
    if req.method == 'POST' :
        name = req.POST.get('name')
        branch = req.POST.get('branch')
        sem = req.POST.get('sem')
        position = req.POST.get('position')
         
        contact = Attendance(name=name, branch=branch,sem=sem,position=position, date = datetime.today())
        contact.save()
        return render(req,"home.html")
    
def fees(req):
    return render(req,"feesstr.html")