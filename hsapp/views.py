from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout, login
from django.contrib import messages
from .models import *
from django.utils.dateparse import parse_date, parse_time


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
    doctors = Doctor.objects.all()
    patients = Patient.objects.all()
    appoint = Appointment.objects.all()
    d = 0
    p = 0
    a = 0
    for i in doctors:
        d += 1
    for i in patients:
        p += 1
    for i in appoint:
        a += 1
    d1 = {"d": d, "p": p, "a": a}

    return render(request, "index.html", d1)


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
    if not request.user.is_staff:
        return redirect("login")
    d = Doctor.objects.get(id=pid)
    d.delete()
    return redirect("view_doctor")


def View_Patient(request):
    if not request.user.is_staff:
        return redirect("login")
    pat = Patient.objects.all()
    p = {"pat": pat}
    return render(request, "view_patient.html", p)


def Add_Patient(request):
    error = ""
    if not request.user.is_staff:
        return redirect("login")
    if request.method == "POST":
        n = request.POST["name"]
        g = request.POST["gender"]
        m = request.POST["mobile"]
        a = request.POST["area"]
        try:
            Patient.objects.create(name=n, gender=g, mobile=m, area=a)
            error = "no"
        except:
            error = "yes"
    d = {"error": error}
    return render(request, "add_patient.html", d)


def Delete_Patient(request, pid):
    if not request.user.is_staff:
        return redirect("login")
    p = Patient.objects.get(id=pid)
    p.delete()
    return redirect("view_patient")


def View_Appointment(request):
    if not request.user.is_staff:
        return redirect("login")
    appoint = Appointment.objects.all()
    d = {"appoint": appoint}
    return render(request, "view_appointment.html", d)


def Add_appointment(request):

    if request.method == "POST":
        doctor_id = request.POST.get("doctor")
        patient_id = request.POST.get("patient")
        app_date = request.POST.get("app_date")
        app_time = request.POST.get("app_time")

        # Validate input
        if not doctor_id or not patient_id or not app_date or not app_time:
            messages.error(request, "All fields are required.")
            return redirect("add_appointment")

        try:
            doctor = Doctor.objects.get(id=doctor_id)
            patient = Patient.objects.get(id=patient_id)
            app_date = parse_date(app_date)
            app_time = parse_time(app_time)

            Appointment.objects.create(
                doctor=doctor, patient=patient, app_date=app_date, app_time=app_time
            )
            messages.success(request, "Appointment created successfully!")
            return redirect("view_appointment")
        except Doctor.DoesNotExist:
            messages.error(request, "Doctor does not exist.")
        except Patient.DoesNotExist:
            messages.error(request, "Patient does not exist.")
        except ValueError:
            messages.error(request, "Invalid date or time format.")

    doctors = Doctor.objects.all()
    patients = Patient.objects.all()

    return render(
        request, "add_appointment.html", {"doctors": doctors, "patients": patients}
    )


def Delete_Appointment(request, pid):
    if not request.user.is_staff:
        return redirect("login")
    p = Appointment.objects.get(id=pid)
    p.delete()
    return redirect("view_appointment")
