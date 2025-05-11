from django.contrib import admin
from .models import Consultation, Ordonnance, OrdonnanceDetail

# Register your models here.

class ConsultationAdmin(admin.ModelAdmin):
    readonly_fields = ('code_consultation',)

class OrdonnanceAdmin(admin.ModelAdmin):
    readonly_fields = ('code_ordonnance',)


admin.site.register(Consultation, ConsultationAdmin)
admin.site.register(Ordonnance, OrdonnanceAdmin)
admin.site.register(OrdonnanceDetail)

