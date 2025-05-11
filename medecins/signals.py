from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from django.db.models.signals import post_migrate
from django.dispatch import receiver

@receiver(post_migrate)
def create_groups_and_permissions(sender, **kwargs):
    groups_permissions = {
        'Médecin': [
            'view_patient', 'add_patient', 'change_patient',
            'add_consultation', 'change_consultation', 'delete_consultation', 'view_consultation',
            'view_ordonnancedetail', 'add_ordonnancedetail', 'change_ordonnancedetail', 'delete_ordonnancedetail',
            'view_affecterspecialite', 'view_medecin', 'view_specialite', 'view_acte', 'view_typeacte', 'view_medicament',
        ],
        'Secrétaire': [
            'view_patient', 'add_patient', 'change_patient',
            'view_ordonnancedetail', 'view_facturedetail', 'add_ordonnancedetail', 'change_ordonnancedetail', 'delete_ordonnancedetail',
            'view_paiement', 'add_paiement', 'change_paiement', 'delete_paiement',
            'view_secretaire', 'change_secretaire',
        ],
        'Admin': [
            'view_patient', 'add_patient', 'change_patient', 'delete_patient',
            'add_user', 'change_user', 'delete_user', 'view_user',
            'add_facturedetail', 'change_facturedetail', 'delete_facturedetail', 'view_facturedetail',
            'add_consultation', 'change_consultation', 'delete_consultation', 'view_consultation',
            'add_ordonnance', 'change_ordonnance', 'delete_ordonnance', 'view_ordonnance',
            'add_facture', 'change_facture', 'delete_facture', 'view_facture',
            'add_paiement', 'change_paiement', 'delete_paiement', 'view_paiement',
            'add_acte', 'change_acte', 'delete_acte', 'view_acte',
            'view_medicament',
            'add_typeacte', 'change_typeacte', 'delete_typeacte', 'view_typeacte',
            'add_specialite', 'change_specialite', 'delete_specialite', 'view_specialite',
            'add_medecin', 'change_medecin', 'delete_medecin', 'view_medecin',
            'add_affecterspecialite', 'change_affecterspecialite', 'delete_affecterspecialite', 'view_affecterspecialite',
        ]
    }

    for group_name, permissions in groups_permissions.items():
        group, created = Group.objects.get_or_create(name=group_name)
        if created:
            print(f"Groupe {group_name} créé")

        for perm_codename in permissions:
            try:
                permission = Permission.objects.get(codename=perm_codename)
                group.permissions.add(permission)
            except Permission.DoesNotExist:
                print(f"⚠ Permission {perm_codename} introuvable")

        group.save()
