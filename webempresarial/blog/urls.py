from django.urls import path
from . import views as bv

urlpatterns = [
    path('', bv.blog, name='blog'),
    path('category/<int:category_id>', bv.category, name='category')
]
