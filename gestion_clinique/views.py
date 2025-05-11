from django.contrib import messages
from django import forms
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User

from consultations.models import Consultation
from gestion_clinique.form import PatientForm, ConsultationForm
from patients.models import Patient


@login_required
def user_dashboard_redirect_view(request):
    user = request.user
    context = {} 

    if user.groups.filter(name='Admin').exists():
        return render(request, '/admin/', context)
    elif user.groups.filter(name='Médecin').exists():
        # Si vous avez des infos spécifiques au dashboard médecin, ajoutez-les au contexte
        # Par exemple, récupérer des statistiques spécifiques au médecin
        # context['nombre_patients_medecin'] = Patient.objects.filter(medecin_referent=user).count()
        return render(request, 'dashboards/medecin_dashboard.html', context) # Assurez-vous que ce chemin est correct
    elif user.groups.filter(name='Secrétaire').exists():
        return render(request, 'dashboards/secretaire_dashboard.html', context)
    else:
        return render(request, 'dashboards/default_dashboard.html', context)


@login_required
def user_profile_view(request):
    return render(request, 'profil/user_profile_view.html', {'user_profile_view': request.user})

@login_required
def user_profile_edit_view(request):
    if request.method == 'POST':
        # Créez un formulaire spécifique pour ne modifier que certains champs
        # par ex. first_name, last_name, email. Ne pas utiliser UserChangeForm directement
        # sans précaution car il peut permettre de changer des choses sensibles.
        # Exemple avec un formulaire simple :
        class ProfileEditForm(forms.ModelForm):
             class Meta:
                 model = User
                 fields = ['username'] # Champs modifiables
        
        form = ProfileEditForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Votre profil a été mis à jour avec succès !')
            return redirect('user_profile_view')
    else:
        form = ProfileEditForm(instance=request.user)
    return render(request, 'profil/user_profile_edit.html', {'form': form})

@login_required
def patient_list_view(request):
    patients_list = Patient.objects.all() 
    # context = {'patients': patients}
    # return render(request, 'patients/patient_list.html', context) # Créez ce template plus tard

    # Ou utilisez une page générique pour l'instant
    context = {
        'page_title': "Liste des Patients",
        'patients': patients_list,
    }
    # Assurez-vous d'avoir un template 'gestion/generic_management_page.html'
    # ou changez le chemin vers un template existant.
    return render(request, 'patients/patient_list.html', context)

@login_required
def patient_add_view(request): # Ceci est la vue pour /patients/add/
    if request.method == 'POST':
        form = PatientForm(request.POST, request.FILES or None) # Utilisez PatientForm ici
        if form.is_valid():
            form.save()
            # messages.success(request, "Patient ajouté avec succès !")
            return redirect('patient_list') # Redirige vers la liste des patients
    else:
        form = PatientForm() # Utilisez PatientForm ici aussi pour une requête GET

    context = {
        'page_title': "Ajouter un Nouveau Patient",
        'form': form
    }
    # Assurez-vous que ce template existe et qu'il est au bon endroit
    return render(request, 'patients/patient_add.html', context)

@login_required
def patient_detail_view(request, pk): # pk vient de l'URL
    patient = get_object_or_404(Patient, pk=pk)
    consultations_patient = Consultation.objects.filter(patient=patient) # Si vous avez un modèle de consultation
    context = {
        'page_title': f"Dossier Patient - {patient.prenom} {patient.nom}",
        'patient': patient,
        # 'consultations_patient': consultations_patient,
    }
    return render(request, 'patients/patient_detail.html', context) # Créez ce template

@login_required
def patient_edit_view(request, pk):
    patient_instance = get_object_or_404(Patient, pk=pk)

    if request.method == 'POST':
        form = PatientForm(request.POST, request.FILES or None, instance=patient_instance)
        if form.is_valid():
            form.save()
            # C'EST ICI QUE L'ERREUR SE PRODUIT SI 'messages' N'EST PAS LE BON OBJET
            messages.success(request, f"Les informations du patient '{patient_instance.prenom} {patient_instance.nom}' ont été mises à jour avec succès.")
            return redirect('patient_detail', pk=patient_instance.pk)
        else:
            # Et potentiellement ici aussi si vous ajoutez messages.error()
            messages.error(request, "Veuillez corriger les erreurs ci-dessous.") # EXEMPLE
    else:
        form = PatientForm(instance=patient_instance)

    context = {
        'form': form,
        'patient': patient_instance,
    }
    return render(request, 'patients/patient_edit.html', context)

@login_required
def patient_delete_view(request, pk):
    patient = get_object_or_404(Patient, pk=pk)
    if request.method == 'POST': # Confirmer la suppression
        nom_patient = f"{patient.prenom} {patient.nom}"
        patient.delete()
        messages.success(request, f"Le patient {nom_patient} a été supprimé avec succès.")
        return redirect('gestion_clinique:patient_list')
    

@login_required
def ordonnance_list_view(request):
    context = {'page_title': "Liste des Ordonnances (en construction)"}
    return render(request, 'ordonnances/ordonnance_list.html', context)

@login_required
def specialty_view(request):
    context = {'page_title': "Mes Spécialités (en construction)"}
    return render(request, 'speciality/spaecialty.html', context)

@login_required
def acte_list_view(request):
    context = {'page_title': "Actes Médicaux (en construction)"}
    return render(request, 'actes/acte_list.html', context)

@login_required
def medicament_list_view(request):
    context = {'page_title': "Médicaments (en construction)"}
    return render(request, 'medicaments/medicament_list.html', context)


@login_required
def consultation_list_view(request):
    context = {'page_title': "Liste des Consultations (en construction)"}
    return render(request, 'consultations/consultation_list.html', context)

@login_required
def consultation_add_for_patient_view(request, pk):
    patient = get_object_or_404(Patient, pk=pk)

    context = {
        'page_title': f"Nouvelle Consultation pour {patient.prenom} {patient.nom}",
        'patient': patient,
        # 'form': form_consultation,
    }
    # Créez un template spécifique pour le formulaire de consultation
    return render(request, 'consultations/consultation_add.html', context)




def consultation_create_view(request, pk):
    patient = get_object_or_404(Patient, pk=pk)
    
    if request.method == "POST":
        form = ConsultationForm(request.POST)
        if form.is_valid():
            consultation = form.save(commit=False)
            consultation.patient = patient
            consultation.save()
            form.save_m2m()  # pour les champs many-to-many comme actes
            return redirect('patient_detail', pk=patient.pk)
    else:
        form = ConsultationForm()
    
    return render(request, 'consultation/consultation_form.html', {
        'form': form,
        'patient': patient
    })