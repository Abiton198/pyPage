# Generated by Django 4.1.7 on 2023-03-27 08:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("destinations", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Hotel",
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
                ("location", models.CharField(max_length=50)),
                ("image_url", models.CharField(max_length=2085)),
                ("name", models.CharField(max_length=50)),
            ],
        ),
    ]