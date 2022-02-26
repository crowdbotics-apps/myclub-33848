from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _


class User(AbstractUser):
    # WARNING!
    """
    Some officially supported features of Crowdbotics Dashboard depend on the initial
    state of this User model (Such as the creation of superusers using the CLI
    or password reset in the dashboard). Changing, extending, or modifying this model
    may lead to unexpected bugs and or behaviors in the automated flows provided
    by Crowdbotics. Change it at your own risk.


    This model represents the User instance of the system, login system and
    everything that relates with an `User` is represented by this model.
    """
    name = models.CharField(
        null=True,
        blank=True,
        max_length=255,
    )
    prenom = models.CharField(
        null=True,
        blank=True,
        max_length=16,
    )
    prenomnom = models.CharField(
        null=True,
        blank=True,
        max_length=256,
    )
    adresse = models.CharField(
        null=True,
        blank=True,
        max_length=256,
    )
    email = models.EmailField(
        null=True,
        blank=True,
        max_length=254,
    )
    telephone = models.PositiveIntegerField(
        null=True,
        blank=True,
    )
    licence = models.PositiveIntegerField(
        null=True,
        blank=True,
    )
    datenaissance = models.DateField(
        null=True,
        blank=True,
    )
    nbanneeclub = models.SmallIntegerField(
        null=True,
        blank=True,
    )
    nbanneepratique = models.SmallIntegerField(
        null=True,
        blank=True,
    )
    photo = models.URLField(
        null=True,
        blank=True,
    )
    datemodification = models.DateField(
        null=True,
        blank=True,
    )
    tuteurde = models.TextField(
        null=True,
        blank=True,
    )
    evenements = models.ManyToManyField(
        "home.Evenements",
        blank=True,
        related_name="user_evenements",
    )
    role = models.ManyToManyField(
        "home.Listerole",
        blank=True,
        related_name="user_role",
    )

    def get_absolute_url(self):
        return reverse("users:detail", kwargs={"username": self.username})
