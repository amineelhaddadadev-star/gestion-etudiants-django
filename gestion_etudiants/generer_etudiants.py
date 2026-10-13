import csv
import random
from datetime import date, timedelta

noms = [
"Alami", "Benali", "Idrissi", "Tazi", "Alaoui",
"Fassi", "Bennani", "Amrani", "Lahlou", "Chraibi",
"Berrada", "Tahiri", "Naciri", "Ziani", "Saidi",
"Mansouri", "Rami", "Kettani", "Ziani", "Mernissi"
]

prenoms = [
"Youssef", "Sara", "Adam", "Salma", "Amine",
"Aya", "Hamza", "Imane", "Omar", "Nour",
"Mehdi", "Lina", "Anas", "Meryem", "Zakaria",
"Hajar", "Yassine", "Kawtar", "Ilyas", "Sofia"
]

specialites = [
("Informatique", "1ère année"),
("EE", "1ère année"),
("Messagerie", "1ère année"),
("Technique", "1ère année"),
("EE", "2ème année"),
("Messagerie", "2ème année"),
("Technique", "2ème année"),
("Informatique", "2ème année"),
]

random.seed(42)

with open("etudiants.csv", "w", newline="", encoding="utf-8-sig") as fichier:
 writer = csv.writer(fichier, delimiter=";")

writer.writerow([
    "nom",
    "prenom",
    "age",
    "date_naissance",
    "specialite",
    "annee"
])

for i in range(100):
    annee_naissance = random.randint(2000, 2007)
    mois_naissance = random.randint(1, 12)

    premier_jour = date(annee_naissance, mois_naissance, 1)

    if mois_naissance == 12:
        dernier_jour = 31
    else:
        dernier_jour = (
            date(annee_naissance, mois_naissance + 1, 1)
            - timedelta(days=1)
        ).day

    jour_naissance = random.randint(1, dernier_jour)

    naissance = date(
        annee_naissance,
        mois_naissance,
        jour_naissance
    )

    aujourd_hui = date.today()
    age = aujourd_hui.year - naissance.year

    if (aujourd_hui.month, aujourd_hui.day) < (
        naissance.month, naissance.day
    ):
        age -= 1

    specialite, annee = random.choice(specialites)

    writer.writerow([
        random.choice(noms),
        random.choice(prenoms),
        age,
        naissance.isoformat(),
        specialite,
        annee
    ])

print("Fichier etudiants.csv créé avec succès : 100 étudiants.")