from django.contrib import admin
from django.urls import path
from hsapp.views import *

urlpatterns = [
    path("admin/", admin.site.urls),
    path("about/", About, name="about"),
    path("contact/", Contact, name="contact"),
    path("navigation/", Navigation, name="navigation"),
    path("", Index, name="home"),
    path("a_login/", Login, name="login"),
    path("a_logout/", Logout_admin, name="logout"),
    path("view_doctor/", View_Doctor, name="view_doctor"),
    path("add_doctor/", Add_Doctor, name="add_doctor"),
    path("delete_doctor(<int:pid>)", Delete_Doctor, name="delete_doctor"),
    path("view_patient/", View_Patient, name="view_patient"),
    path("add_patient/", Add_Patient, name="add_patient"),
    path("delete_patient(<int:pid>)", Delete_Patient, name="delete_patient"),
    path("view_appointment/", View_Appointment, name="view_appointment"),
    path("add_appointment/", Add_appointment, name="add_appointment"),
    path(
        "delete_appointment/<int:pid>/",
        Delete_Appointment,
        name="delete_appointment",
    ),
]
