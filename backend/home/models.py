from django.conf import settings
from django.db import models


class Utilisateurs(models.Model):
    "Generated Model"
    prenom = models.CharField(
        max_length=16,
        blank=True,
    )
    nom = models.CharField(
        max_length=16,
        blank=True,
    )
    prenomnom = models.CharField(
        max_length=32,
        blank=True,
    )
    role = models.CharField(
        max_length=50,
        blank=True,
    )
    license = models.IntegerField(
        null=True,
        blank=True,
    )
    email = models.EmailField(
        max_length=254,
        null=True,
        blank=True,
    )
    adresse = models.TextField(
        null=True,
        blank=True,
    )
    datenaissance = models.DateField(
        null=True,
        blank=True,
    )
    telephone = models.CharField(
        max_length=256,
        null=True,
        blank=True,
    )
    idutilisateur = models.UUIDField(
        null=True,
        blank=True,
    )
    nbanneeclub = models.PositiveIntegerField(
        null=True,
        blank=True,
    )
    nbanneepratique = models.PositiveIntegerField(
        null=True,
        blank=True,
    )


class Listecategorie(models.Model):
    "Generated Model"
    nom = models.CharField(
        max_length=10,
    )
