# gestion_clinique/urls.py
from django.urls import include, path
from . import views 
urlpatterns = [    

    path('', include('gestion_clinique.urls', namespace='gestion_clinique')),

]