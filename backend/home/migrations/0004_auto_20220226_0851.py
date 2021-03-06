# Generated by Django 2.2.26 on 2022-02-26 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0003_auto_20220225_1628"),
    ]

    operations = [
        migrations.CreateModel(
            name="Articles",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("titre", models.CharField(max_length=256)),
                ("description", models.TextField()),
                ("photo", models.URLField()),
                ("datemodification", models.DateField()),
                ("modifiepar", models.CharField(max_length=256)),
                (
                    "categories",
                    models.ManyToManyField(
                        blank=True,
                        related_name="articles_categories",
                        to="home.Articles",
                    ),
                ),
            ],
        ),
        migrations.DeleteModel(
            name="Utilisateurs",
        ),
    ]
