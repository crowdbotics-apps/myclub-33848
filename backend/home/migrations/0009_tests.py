# Generated by Django 2.2.26 on 2022-02-26 11:21

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('home', '0008_rencontres_buteureqclub'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tests',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre', models.CharField(max_length=256)),
                ('date', models.DateField()),
                ('evenement', models.ManyToManyField(related_name='tests_evenement', to='home.Evenements')),
                ('joueur', models.ManyToManyField(related_name='tests_joueur', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
