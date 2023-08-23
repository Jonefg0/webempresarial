from django.urls import path
from . import views as sv

urlpatterns = [
    path('', sv.services, name='services'),
]
