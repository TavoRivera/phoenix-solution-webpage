# Generated by Django 5.1.5 on 2025-02-04 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("website", "0005_servicio"),
    ]

    operations = [
        migrations.AddField(
            model_name="servicio",
            name="imagen",
            field=models.ImageField(
                blank=True, null=True, upload_to="images/servicios"
            ),
        ),
    ]
