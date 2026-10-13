from django.db import models
ANNEE_CHOICES = [
    ('1ere', '1ère année'),
    ('2eme', '2ème année'),
]

SPECIALITE_CHOICES = [
    ('informatique', 'Informatique'),
    ('EE', 'EE'),
    ('messagerie', 'Messagerie'),
    ('technique', 'Technique'),
]

OPTION_CHOICES = [
    ('reseau', 'Réseau informatique'),
    ('genie_logiciel', 'Génie logiciel'),
    ('cybersecurite', 'Cybersécurité'),
    ('infographie', 'Infographie'),
]

class Annee(models.Model):
    nom = models.CharField(max_length=20)

    def __str__(self):
        return self.nom

class Specialite(models.Model):
    nom = models.CharField(max_length=100)
    annee = models.ForeignKey(Annee, on_delete=models.CASCADE)

    def __str__(self):
        return self.nom

class Option(models.Model):
    nom = models.CharField(max_length=100)
    specialite = models.ForeignKey(Specialite, on_delete=models.CASCADE)

    def __str__(self):
        return self.nom
            
class Etudiant(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    age = models.IntegerField()
    date_naissance = models.DateField(null=True, blank=True)
    specialite = models.ForeignKey(
        Specialite,
        on_delete=models.CASCADE
    )

    option = models.ForeignKey(
        Option,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    def clean(self):
      from django.core.exceptions import ValidationError

      super().clean()

      if self.option and self.specialite:
        if self.option.specialite_id != self.specialite_id:
            raise ValidationError({
                'option': "Cette option n'appartient pas à cette spécialité."
            })

    def __str__(self):
        return f"{self.nom} {self.prenom}"
# Create your models here.
