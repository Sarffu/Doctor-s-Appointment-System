from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout, login
from django.contrib import messages
from .models import *


# Create your views here.
def About(request):
    return render(request, "about.html")


def Navigation(request):
    return render(request, "navigation.html")


def Contact(request):
    return render(request, "contact.html")


def Index(request):
    if not request.user.is_staff:
        return redirect("login")
    return render(request, "index.html")


def Login(request):
    if request.method == "POST":
        username = request.POST.get("aname")
        password = request.POST.get("pwd")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            messages.error(request, "Incorrect login credentials, try again later.")
            return render(request, "login.html", {"error": "yes"})
    return render(request, "login.html")


def Logout_admin(request):
    if not request.user.is_staff:
        return redirect("login")
    logout(request)
    return redirect("login")


def View_Doctor(request):
    if not request.user.is_staff:
        return redirect("login")
    doc = Doctor.objects.all()
    d = {"doc": doc}
    return render(request, "view_doctor.html", d)


def Add_Doctor(request):
    error = ""
    if not request.user.is_staff:
        return redirect("login")
    if request.method == "POST":
        n = request.POST["name"]
        m = request.POST["mobile"]
        sp = request.POST["special"]
        try:
            Doctor.objects.create(name=n, mobile=m, specialization=sp)
            error = "no"  # Success
        except:
            error = "yes"  # Failure
    d = {"error": error}
    return render(request, "add_doctor.html", d)

def Delete_Doctor(request, pid):
    if not request.user.is_staff :
        return redirect('login')
    d = Doctor.objects.get(id=pid)
    d.delete()
    return redirect('view_doctor')
