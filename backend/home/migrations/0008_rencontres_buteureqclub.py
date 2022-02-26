# Generated by Django 2.2.26 on 2022-02-26 11:08

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('home', '0007_rencontres'),
    ]

    operations = [
        migrations.AddField(
            model_name='rencontres',
            name='buteureqclub',
            field=models.ManyToManyField(blank=True, related_name='rencontres_buteureqclub', to=settings.AUTH_USER_MODEL),
        ),
    ]