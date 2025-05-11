from django import forms

from consultations.models import Consultation
from medecins.models import Medecin
from parametrage.models import Acte
from patients.models import Patient
# Importez votre modèle Patient depuis l'emplacement correct
# Si Patient est dans gestion_clinique.models :
# Si Patient est dans patients_app.models :
# from patients_app.models import Patient

class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        # Spécifiez les champs que vous voulez dans le formulaire
        fields = ['nom', 'prenom', 'date_naissance', 'civilite', 'telephone', 'adresse', 'email', 'code', ] # Adaptez avec vos champs réels
        # Vous pouvez aussi utiliser fields = '__all__' mais c'est moins sécurisé
        # Vous pouvez aussi ajouter des widgets ou personnaliser les labels ici
        widgets = {
            'date_naissance': forms.DateInput(attrs={'type': 'date'}),
            # Ajoutez d'autres widgets si nécessaire
        }
        labels = {
            'numero_assurance_maladie': 'Numéro d\'assurance maladie',
            # Personnalisez d'autres labels
        }

class ConsultationForm(forms.ModelForm):
    date_fin_validite_consultation = forms.DateTimeField(
        widget=forms.DateTimeInput(
            attrs={'type': 'datetime-local', 'class': 'form-control'},
            format='%Y-%m-%dT%H:%M'
        ),
        label="Date et heure de fin de validité",
        input_formats=['%Y-%m-%dT%H:%M', '%Y-%m-%d %H:%M:%S', '%Y-%m-%d %H:%M'],
        required=True # Ou False si optionnel
    )

    actes = forms.ModelMultipleChoiceField(
        queryset=Acte.objects.all().order_by('libelle_acte'), # Ou 'code_acte'
        widget=forms.SelectMultiple(attrs={'class': 'form-select', 'size': '8'}),
        label="Actes médicaux effectués",
        required=False, # Car blank=True dans votre modèle Acte <-> Consultation
        help_text="Maintenez Ctrl (ou Cmd) pour sélectionner plusieurs actes."
    )

    class Meta:
        model = Consultation
        fields = ['code_consultation', 'date_fin_validite_consultation', 'actes']
        widgets = {
            'date_fin_validite_consultation': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'actes': forms.SelectMultiple(attrs={'class': 'form-select'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Appliquer des classes CSS par défaut si besoin (optionnel)
        for field_name, field in self.fields.items():
            if not field.widget.attrs.get('class'):
                if isinstance(field.widget, forms.TextInput):
                    field.widget.attrs.update({'class': 'form-control'})
                elif isinstance(field.widget, forms.SelectMultiple): # Déjà fait explicitement mais bon à avoir
                    field.widget.attrs.update({'class': 'form-select'})