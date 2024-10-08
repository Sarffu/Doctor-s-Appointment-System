from django.db import models

# Create your models here.


class Doctor(models.Model):
    name = models.CharField(max_length=50)
    mobile = models.IntegerField()
    specialization = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Patient(models.Model):
    name = models.CharField(max_length=50)
    gender = models.CharField(max_length=10)
    mobile = models.IntegerField()
    area = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Appointment(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    app_date = models.DateField()
    app_time = models.TimeField()

    def __str__(self):
        return f"{self.doctor.name} , {self.patient.name}"
