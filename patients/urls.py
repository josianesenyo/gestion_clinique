# gestion_clinique/urls.py
from django.urls import path
from . import views 
urlpatterns = [
    
    path('patients/', views.patient_list_view, name='patient_list'),
]

