from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import render, redirect, reverse
from django.http import HttpResponseForbidden, HttpResponse

# Create your views here.

def is_medecin(user):
    return user.groups.filter(name='Médecin').exists()

@login_required
def dashboard_medecin(request):
    return render(request, 'medecins/dashboard.html')



# medecins/views.py # Ajoutez HttpResponse
# ... autres imports pour les vues des médecins ...

@login_required
def user_dashboard_redirect_view(request):
    user = request.user

    if user.is_superuser:
        return redirect(reverse('admin:index'))

    # Le modèle Medecin est directement lié à User via utilisateur, donc l'accesseur inverse est user.medecin
    if hasattr(user, 'medecin') and user.medecin:
        return redirect(reverse('medecins:dashboard'))
    # Si Secretaire est un utilisateur et a un lien OneToOne 'utilisateur'
    elif hasattr(user, 'secretaire') and user.secretaire: # Adaptez 'secretaire' si le nom de la relation est différent
        return redirect(reverse('secretaires:dashboard'))
    elif user.is_staff: # Pour le staff qui n'a pas de profil spécifique mais accès à l'admin
        return redirect(reverse('admin:index'))
    else:
        # Fallback pour les utilisateurs sans rôle défini ou une page d'accueil générique
        # Rediriger vers la page d'accueil du site (définie dans les URLs du projet)
        return redirect(reverse('home_page')) # Assurez-vous que 'home_page' est défini

# ... vos autres vues de l'application medecins ...
# (medecin_dashboard_view, manage_patients_view, etc.)
@login_required
def medecin_dashboard_view(request):
    if not (hasattr(request.user, 'medecin') and request.user.medecin):
        return HttpResponseForbidden("Accès refusé.")
    return render(request, 'medecin/dashboard.html', {'page_title': "Tableau de Bord Médecin"})

# Ajoutez une vue pour la page d'accueil si elle n'existe pas ailleurs
def home_page_view(request):
    return render(request, 'home.html') # Assurez-vous que templates/home.html existe