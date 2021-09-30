from django.db import models
import datetime

class Marque(models.Model):
    marque = models.CharField(max_length=300)
    def __str__(self):
        return self.marque


class Modele(models.Model):
    modele = models.CharField(max_length=300)
    def __str__(self):
        return self.modele

class Etat(models.Model):
    etat = models.CharField(max_length=300)
    def __str__(self):
        return self.etat

    
class Voiture(models.Model):
    id = models.BigAutoField(primary_key=True,)
    TRANSMISSION = (
        ('AUTOMATIQUE','AUTOMATIQUE'),
        ('MANUEL', 'MANUEL'),
        ('HYBRIDE', 'HYBRIDE'),
    )
    CARBURANT = (
        ('ESSENCE','ESSENCE'),
        ('GASOIL', 'GASOIL'),
    )
    YEAR_CHOICES = []
    for r in range(1980, (datetime.datetime.now().year+1)):
        YEAR_CHOICES.append((r,r))
    marque = models.ForeignKey('Marque', on_delete=models.CASCADE, null=True, blank=True)
    modele = models.ForeignKey('Modele', on_delete=models.CASCADE, null=True, blank=True)
    etat = models.ForeignKey('Etat', on_delete=models.CASCADE, null=True, blank=True)
    transmission = models.CharField(max_length=300, choices = TRANSMISSION)
    carburant = models.CharField(max_length=300, choices = CARBURANT)
    annee = models.IntegerField(choices=YEAR_CHOICES)
    prix = models.CharField(max_length=300)
    kilometrage = models.IntegerField()
    photo_face = models.ImageField(upload_to='images/', null=True, blank=True)
    photo_longueur1 = models.ImageField(upload_to='images/', null=True, blank=True)
    photo_longueur2 = models.ImageField(upload_to='images/', null=True, blank=True)
    photo_arriere = models.ImageField(upload_to='images/', null=True, blank=True)
    photo_photo_tableau = models.ImageField(upload_to='images/', null=True, blank=True)
    photo_option1 = models.ImageField(upload_to='images/', null=True, blank=True)
    photo_option2 = models.ImageField(upload_to='images/', null=True, blank=True)
    photo_option3 = models.ImageField(upload_to='images/', null=True, blank=True)
    photo_option4 = models.ImageField(upload_to='images/', null=True, blank=True)    
    photo_option5 = models.ImageField(upload_to='images/', null=True, blank=True)    
    photo_moteur = models.ImageField(upload_to='images/', null=True, blank=True)
    photo_carte_grise = models.ImageField(upload_to='images/', null=True, blank=True)
    photo_assurance = models.ImageField(upload_to='images/', null=True, blank=True)
    photo_defaut1 = models.ImageField(upload_to='images/', null=True, blank=True)
    photo_defaut2 = models.ImageField(upload_to='images/', null=True, blank=True)
    photo_defaut3 = models.ImageField(upload_to='images/', null=True, blank=True)
    photo_defaut4 = models.ImageField(upload_to='images/', null=True, blank=True)
    photo_defaut5 = models.ImageField(upload_to='images/', null=True, blank=True)
    Description = models.TextField()
    date_ajout = models.DateField()
    def __str__(self):
        return str(self.marque)+ " " + str(self.modele) + " " + str(self.date_ajout)


