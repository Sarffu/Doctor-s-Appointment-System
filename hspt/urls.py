from django.contrib import admin
from django.urls import path
from hsapp.views import *

urlpatterns = [
    path("admin/", admin.site.urls),
    path("about/", About, name="about"),
    path("navigation/", Navigation, name="navigation"),
]
