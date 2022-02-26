# Generated by Django 2.2.26 on 2022-02-26 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_auto_20220226_1037'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rencontres',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre', models.CharField(max_length=256)),
                ('equipeclub', models.CharField(max_length=256)),
                ('nbbutmarqueequipeclub', models.PositiveSmallIntegerField()),
                ('equipeadverse', models.CharField(max_length=256)),
                ('nbbutmarqueequipeadverse', models.PositiveSmallIntegerField()),
                ('adomicile', models.BinaryField()),
                ('evenement', models.ManyToManyField(related_name='rencontres_evenement', to='home.Evenements')),
            ],
        ),
    ]
