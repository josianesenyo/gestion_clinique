"""
URL configuration for gestion_clinique project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from .views import user_dashboard_redirect_view, user_dashboard_redirect_view, user_profile_edit_view, user_profile_view
from django.conf.urls.static import static 
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('', include('medecins.urls')),
    path('dashboard_redirect/', user_dashboard_redirect_view, name='user_dashboard_redirect'),
    path('profil/', views.user_profile_view, name='user_profile'),
    path('profil/modifier/', views.user_profile_edit_view, name='user_profile_edit'),
    path('consultations/', views.consultation_list_view, name='consultation_list'),
    path('ordonnances/', views.ordonnance_list_view, name='ordonnance_list'),
    path('specialites/', views.specialty_view, name='specialite_list'),
    path('actes/', views.acte_list_view, name='acte_list'),
    path('medicaments/', views.medicament_list_view, name='medicament_list'),
    
    path('patients/', views.patient_list_view, name='patient_list'),
    path('profil/modifier/', views.user_profile_edit_view, name='user_profile_edit'),
    path('patients/add/', views.patient_add_view, name='patient_add'),
    
    path('patients/<int:pk>/details/', views.patient_detail_view, name='patient_detail'),

    path('patients/<int:pk>/edit/', views.patient_edit_view, name='patient_edit'),   # NOUVEAU
    path('patients/<int:pk>/delete/', views.patient_delete_view, name='patient_delete'),


    # ... vos autres URLs (prescriptions, specialites, etc.) ...
    path('prescriptions/', views.ordonnance_list_view, name='prescription_list'),
    path('specialites/', views.specialty_view, name='specialty_list'),
    path('actes-medicaux/', views.acte_list_view, name='medical_act_list'),
    path('medicaments/', views.medicament_list_view, name='medication_list'),


    path('consultations/', views.consultation_list_view, name='consultation_list'),
    # URL pour créer une consultation (sans patient_id dans l'URL)
    path('consultation/creer/', views.consultation_create_view, name='consultation_create'),
    # URL pour ajouter une consultation à un patient spécifique
    path('patients/<int:pk>/consultation/ajouter/', views.consultation_add_for_patient_view, name='consultation_add_for_patient'),
    ]
