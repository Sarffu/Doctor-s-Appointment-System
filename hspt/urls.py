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
]
