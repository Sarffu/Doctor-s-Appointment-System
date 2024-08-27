from django.contrib import admin
from .models import *


# Register your models here.
@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ["name", "mobile", "specialization"]


@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ["name", "gender", "mobile", "area"]


@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ["doctor", "patient", "app_date", "app_time"]
