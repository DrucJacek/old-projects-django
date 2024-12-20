# Generated by Django 4.2.16 on 2024-12-03 07:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Kadra",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("imie", models.CharField(max_length=100)),
                ("nazwisko", models.CharField(max_length=100)),
                ("stanowisko", models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name="Uslugi",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nazwa", models.CharField(max_length=100)),
                ("cena", models.PositiveSmallIntegerField()),
                (
                    "kadra",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="beautyapp.kadra",
                    ),
                ),
            ],
        ),
    ]
