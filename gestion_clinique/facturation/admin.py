from django.contrib import admin
from .models import Facture, FactureDetail, Paiement


# Register your models here.
class FactureAdmin(admin.ModelAdmin):
    readonly_fields = ('code_facture',)


admin.site.register(Facture, FactureAdmin)
admin.site.register(FactureDetail)
admin.site.register(Paiement)
