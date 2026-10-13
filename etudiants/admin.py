from django.contrib import admin
from .models import Etudiant, Annee, Specialite, Option

@admin.register(Etudiant)
class EtudiantAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'nom',
        'prenom',
        'specialite',
        'option',
    )


    search_fields = ('nom', 'prenom')
    list_filter = ('specialite',)

admin.site.register(Annee)
admin.site.register(Specialite)
admin.site.register(Option)

# Register your models here.
