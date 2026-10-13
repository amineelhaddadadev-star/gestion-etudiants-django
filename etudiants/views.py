from django.shortcuts import render, redirect
from django.core.exceptions import ValidationError
from django.db.models import Q
from .models import Etudiant, Specialite, Option, Annee


def accueil(request):
    """Page d'accueil principale"""
    return render(request, 'etudiants/accueil.html')


def liste_etudiants(request):
    """Affichage de la liste complète des étudiants"""
    etudiants = Etudiant.objects.select_related(
        'specialite',
        'option',
        'specialite__annee'
    ).all()
    
    return render(
        request,
        'etudiants/etudiants.html',
        {'etudiants': etudiants}
    )


def rechercher_etudiant(request):
    """Recherche d'un étudiant par nom ou prénom"""
    query = request.GET.get('q', '').strip()
    etudiants = Etudiant.objects.select_related(
        'specialite',
        'option',
        'specialite__annee'
    )

    if query:
        etudiants = etudiants.filter(
            Q(nom__icontains=query) |
            Q(prenom__icontains=query)
        )

    return render(
        request,
        'etudiants/rechercher.html',
        {
            'etudiants': etudiants,
            'query': query
        }
    )


def ajouter_etudiant(request):
    """Ajout d'un nouvel étudiant avec validations complètes"""
    annees = Annee.objects.all()
    specialites = Specialite.objects.select_related('annee').all()
    options = Option.objects.select_related('specialite').all()

    contexte = {
        'annees': annees,
        'specialites': specialites,
        'options': options,
    }

    if request.method == 'POST':
        nom = request.POST.get('nom', '').strip()
        prenom = request.POST.get('prenom', '').strip()
        age_saisi = request.POST.get('age', '').strip()
        annee_id = request.POST.get('annee', '').strip()
        specialite_id = request.POST.get('specialite', '').strip()
        option_id = request.POST.get('option', '').strip()

        contexte.update({
            'nom_saisi': nom,
            'prenom_saisi': prenom,
            'age_saisi': age_saisi,
            'annee_selectionnee': annee_id,
            'specialite_selectionnee': specialite_id,
            'option_selectionnee': option_id,
        })

        # Vérification des champs obligatoires
        if not all([nom, prenom, age_saisi, annee_id, specialite_id]):
            contexte['error'] = 'Veuillez remplir tous les champs obligatoires.'
            return render(request, 'etudiants/ajouter.html', contexte)

        try:
            # Validation de l'âge
            age = int(age_saisi)
            if age < 1 or age > 120:
                raise ValueError

            # Récupération de l'année et de la spécialité liée
            annee = Annee.objects.get(pk=annee_id)
            specialite = Specialite.objects.get(
                pk=specialite_id,
                annee=annee
            )

            # Gestion spécifique de l'option (Obligatoire pour Informatique)
            if specialite.nom.strip().lower() == 'informatique':
                if not option_id:
                    contexte['error'] = 'Veuillez choisir une option pour la spécialité Informatique.'
                    return render(request, 'etudiants/ajouter.html', contexte)

                option = Option.objects.get(
                    pk=option_id,
                    specialite=specialite
                )
            else:
                option = None

            # Création et sauvegarde de l'étudiant
            etudiant = Etudiant(
                nom=nom,
                prenom=prenom,
                age=age,
                specialite=specialite,
                option=option,
                date_naissance=None
            )

            etudiant.full_clean()
            etudiant.save()

            return redirect('liste_etudiants')

        except (Annee.DoesNotExist, Specialite.DoesNotExist):
            contexte['error'] = "L'année ou la spécialité sélectionnée est invalide."

        except Option.DoesNotExist:
            contexte['error'] = "L'option sélectionnée ne correspond pas à cette spécialité."

        except ValueError:
            contexte['error'] = "Veuillez saisir un âge valide entre 1 et 120."

        except ValidationError as erreur:
            contexte['error'] = str(erreur)

        return render(request, 'etudiants/ajouter.html', contexte)

    return render(request, 'etudiants/ajouter.html', contexte)