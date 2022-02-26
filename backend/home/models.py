from django.conf import settings
from django.db import models


class Listecategorie(models.Model):
    "Generated Model"
    nom = models.CharField(
        max_length=10,
    )
    articles = models.ManyToManyField(
        "home.Articles",
        blank=True,
        related_name="listecategorie_articles",
    )
    users = models.ManyToManyField(
        "users.User",
        blank=True,
        related_name="listecategorie_users",
    )


class Listerole(models.Model):
    "Generated Model"
    nom = models.CharField(
        max_length=16,
    )


class Articles(models.Model):
    "Generated Model"
    titre = models.CharField(
        max_length=256,
    )
    description = models.TextField()
    photo = models.URLField()
    datemodification = models.DateField()
    modifiepar = models.CharField(
        max_length=256,
    )


class Evenements(models.Model):
    "Generated Model"
    titre = models.CharField(
        max_length=256,
    )
    datedebut = models.DateTimeField()
    datefin = models.DateTimeField()
    lieu = models.CharField(
        max_length=256,
    )
    description = models.TextField()
    categorie = models.CharField(
        max_length=256,
        null=True,
        blank=True,
    )
    idevenement = models.UUIDField(
        null=True,
        blank=True,
    )
