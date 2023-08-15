from django.urls import path
from . import views as sv

urlpatterns = [
    path('services', sv.services, name='services'),
]
