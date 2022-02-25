from django.conf import settings
from django.db import models


class Utilisateurs(models.Model):
    "Generated Model"
    prenom = models.CharField(
        blank=True,
        max_length=16,
    )
    nom = models.CharField(
        blank=True,
        max_length=16,
    )
    prenomnom = models.CharField(
        blank=True,
        max_length=32,
    )
    role = models.CharField(
        blank=True,
        max_length=50,
    )
    license = models.IntegerField(
        null=True,
        blank=True,
    )
    email = models.EmailField(
        null=True,
        blank=True,
        max_length=254,
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
        null=True,
        blank=True,
        max_length=256,
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
    photo = models.URLField(
        null=True,
        blank=True,
    )


class Listecategorie(models.Model):
    "Generated Model"
    nom = models.CharField(
        max_length=10,
    )


class Listerole(models.Model):
    "Generated Model"
    nom = models.CharField(
        max_length=16,
    )
