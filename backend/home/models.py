from django.conf import settings
from django.db import models


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
    categories = models.ManyToManyField(
        "home.Articles",
        blank=True,
        related_name="articles_categories",
    )
