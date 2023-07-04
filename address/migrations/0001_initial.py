# Generated by Django 4.2.2 on 2023-07-04 17:37

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Address",
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
                ("country", models.CharField(max_length=40)),
                ("state", models.CharField(max_length=2)),
                ("city", models.CharField(max_length=40)),
                ("road", models.CharField(max_length=120)),
            ],
        ),
    ]
