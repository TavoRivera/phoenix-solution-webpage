# Generated by Django 5.1.5 on 2025-01-23 22:47

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Puesto",
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
                ("nombre", models.CharField(max_length=100, unique=True)),
                ("descripcion", models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="Miembro",
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
                ("nombre", models.CharField(max_length=100)),
                ("correo", models.EmailField(max_length=254, unique=True)),
                ("telefono", models.BigIntegerField()),
                ("descripcion", models.TextField(blank=True, null=True)),
                (
                    "puesto",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="website.puesto"
                    ),
                ),
            ],
        ),
    ]
