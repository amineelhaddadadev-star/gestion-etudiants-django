from django.urls import path
from . import views

urlpatterns = [
    path('', views.accueil, name='accueil'),
    path('etudiants/', views.liste_etudiants, name='liste_etudiants'),
    path('rechercher/', views.rechercher_etudiant, name='rechercher_etudiant'),
    path('ajouter/', views.ajouter_etudiant, name='ajouter_etudiant'),
]