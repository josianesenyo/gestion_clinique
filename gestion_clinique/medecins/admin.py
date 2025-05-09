from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from .models import Medecin, Specialite, AffecterSpecialite

User = get_user_model()  # Utilise le modèle personnalisé défini dans AUTH_USER_MODEL

# Register your models here.

class MedecinAdmin(admin.ModelAdmin):
    readonly_fields = ('code',)

    def save_model(self, request, obj, form, change):
        if not change:  # si on crée un nouveau médecin
            username = f"{obj.nom.lower()}.{obj.prenom.lower()}"
            password = User.objects.make_random_password()
            user = User.objects.create_user(
                username=username,
                password=password,
                first_name=obj.prenom,
                last_name=obj.nom,
                is_active=True
            )
            obj.utilisateur = user  # on suppose que Medecin a un champ OneToOne vers Utilisateur
            obj.save()
            # Ajouter au groupe Médecin
            medecin_group, _ = Group.objects.get_or_create(name='Médecin')
            user.groups.add(medecin_group)
        else:
            super().save_model(request, obj, form, change)

class SpecialiteAdmin(admin.ModelAdmin):
    readonly_fields = ('code',)

admin.site.register(Medecin, MedecinAdmin)
admin.site.register(Specialite, SpecialiteAdmin)
admin.site.register(AffecterSpecialite)
