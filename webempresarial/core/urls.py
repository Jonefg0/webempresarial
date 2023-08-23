from django.urls import path
from . import views as cv

urlpatterns = [
    path("", cv.index,name="home"),
    path("about/", cv.about,name="about"),
    path("store/", cv.store,name="store"),
    path("contact/", cv.contact,name="contact"),
]