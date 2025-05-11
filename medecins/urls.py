from django.urls import path
from .views import dashboard_medecin

urlpatterns = [
    path('/dashboards/medecin/', dashboard_medecin, name='medecin_dashboard'),
]
