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


class Listerole(models.Model):
    "Generated Model"
    nom = models.CharField(
        max_length=16,
    )
    type = models.CharField(
        null=True,
        blank=True,
        max_length=16,
    )
    categorie = models.ManyToManyField(
        "home.Listecategorie",
        blank=True,
        related_name="listerole_categorie",
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
        null=True,
        blank=True,
        max_length=256,
    )
    idevenement = models.UUIDField(
        null=True,
        blank=True,
    )


class Rencontres(models.Model):
    "Generated Model"
    titre = models.CharField(
        max_length=256,
    )
    equipeclub = models.CharField(
        max_length=256,
    )
    nbbutmarqueequipeclub = models.PositiveSmallIntegerField()
    equipeadverse = models.CharField(
        max_length=256,
    )
    nbbutmarqueequipeadverse = models.PositiveSmallIntegerField()
    adomicile = models.BinaryField()
    evenement = models.ManyToManyField(
        "home.Evenements",
        related_name="rencontres_evenement",
    )
    buteureqclub = models.ManyToManyField(
        "users.User",
        blank=True,
        related_name="rencontres_buteureqclub",
    )


class Tests(models.Model):
    "Generated Model"
    titre = models.CharField(
        max_length=256,
    )
    date = models.DateField()
    joueur = models.ManyToManyField(
        "users.User",
        related_name="tests_joueur",
    )
    evenement = models.ManyToManyField(
        "home.Evenements",
        related_name="tests_evenement",
    )
