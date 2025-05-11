from django.contrib import admin
from .models import TypeActe, Acte, Medicament

# Register your models here.
class TypeActeAdmin(admin.ModelAdmin):
    readonly_fields = ('code',)

class ActeAdmin(admin.ModelAdmin):
    readonly_fields = ('code_acte',)

class MedicamentAdmin(admin.ModelAdmin):
    readonly_fields = ('code_medicament',)

admin.site.register(TypeActe, TypeActeAdmin)
admin.site.register(Acte, ActeAdmin)
admin.site.register(Medicament, MedicamentAdmin)
