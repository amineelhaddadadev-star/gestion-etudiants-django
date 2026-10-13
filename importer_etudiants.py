import csv
import os
import django
from datetime import date

os.environ.setdefault(
    "DJANGO_SETTINGS_MODULE",
    "gestion_etudiants.settings"
)

django.setup()

from etudiants.models import Etudiant, Specialite

FICHIER_CSV = "etudiants.csv"

importes = 0
doublons = 0
erreurs = []

with open(
    FICHIER_CSV,
    "r",
    encoding="utf-8-sig",
    newline=""
) as fichier:

    lecteur = csv.DictReader(fichier, delimiter=";")

    # La boucle for doit être indentée à l'intérieur du 'with'
    for numero_ligne, ligne in enumerate(lecteur, start=2):
        try:
            nom = ligne["nom"].strip()
            prenom = ligne["prenom"].strip()
            age = int(ligne["age"])
            date_naissance = date.fromisoformat(
                ligne["date_naissance"].strip()
            )
            nom_specialite = ligne["specialite"].strip()
            annee = ligne["annee"].strip()

            # Rechercher la spécialité dans la base de données
            specialites = Specialite.objects.filter(
                nom__iexact=nom_specialite,
                annee__nom__iexact=annee
            )

            if not specialites.exists():
                raise ValueError(
                    f"Spécialité introuvable : '{nom_specialite}' pour l'année '{annee}'"
                )

            specialite = specialites.first()

            # Vérifier si l'étudiant existe déjà
            existe = Etudiant.objects.filter(
                nom__iexact=nom,
                prenom__iexact=prenom,
                date_naissance=date_naissance,
                specialite=specialite
            ).exists()

            if existe:
                doublons += 1
                continue

            # Ajouter l'étudiant
            Etudiant.objects.create(
                nom=nom,
                prenom=prenom,
                age=age,
                date_naissance=date_naissance,
                specialite=specialite,
                option=None
            )

            importes += 1

        except Exception as erreur:
            erreurs.append(
                f"Ligne {numero_ligne} : {erreur}"
            )

print("\n========== RÉSULTAT ==========")
print(f"Étudiants importés : {importes}")
print(f"Doublons ignorés   : {doublons}")
print(f"Erreurs            : {len(erreurs)}")

for erreur in erreurs:
    print(erreur)

print("==============================")