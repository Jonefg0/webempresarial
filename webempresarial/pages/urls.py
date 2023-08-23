from django.urls import path
from . import views as pv

urlpatterns = [ 
    path('<int:page_id>/<slug:page_slug>/', pv.page, name='page')
]