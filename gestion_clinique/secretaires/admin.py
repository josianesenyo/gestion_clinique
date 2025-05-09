from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from .models import Secretaire

User = get_user_model()

# Register your models here.

@admin.register(Secretaire)
class SecretaireAdmin(admin.ModelAdmin):
    readonly_fields = ('code',)  # Pour griser le champ code dans l’admin
    def save_model(self, request, obj, form, change):
        if not change:
            username = f"{obj.nom.lower()}.{obj.prenom.lower()}"
            password = User.objects.make_random_password()


            user = User.objects.create_user(
                username=username,
                password=password,
                first_name=obj.prenom,
                last_name=obj.nom,
                is_active=True
            )
            obj.utilisateur = user
            obj.save()
            secretaire_group, _ = Group.objects.get_or_create(name='Secretaire')
            user.groups.add(secretaire_group)
        else:
            super().save_model(request, obj, form, change)
