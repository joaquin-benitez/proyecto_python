from django.urls import path
from . import views

urlpatterns = [
    path('hamburguesas/', views.hamburguesas_list, name='hamburguesas_list'),
]
