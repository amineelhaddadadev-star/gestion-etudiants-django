import csv
import random
from datetime import date, timedelta

noms = ["Alami", "Benali", "Idrissi", "Tazi", "Alaoui",
        "Fassi", "Bennani", "Amrani", "Lahlou", "Chraibi"]

prenoms = ["Youssef", "Sara", "Adam", "Salma", "Amine",
           "Aya", "Hamza", "Imane", "Omar", "Nour"]

specialites = ["Informatique", "EE", "Messagerie", "Technique"]

with open("etudiants.csv", "w", newline="", encoding="utf-8-sig") as fichier:
    writer = csv.writer(fichier, delimiter=";")
    writer.writerow(["nom", "prenom", "age", "date_naissance", "specialite"])

    for i in range(100):
        naissance = date(random.randint(2000, 2007), random.randint(1, 12), 1)
        age = date.today().year - naissance.year

        writer.writerow([
            random.choice(noms),
            random.choice(prenoms),
            age,
            naissance.isoformat(),
            random.choice(specialites)
        ])

print("Fichier etudiants.csv créé avec 100 étudiants de test.")