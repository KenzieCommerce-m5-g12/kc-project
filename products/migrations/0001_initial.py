# Generated by Django 4.2.2 on 2023-06-30 16:20

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Product",
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
                ("name", models.CharField(max_length=140)),
                ("category", models.CharField(max_length=20)),
                ("price", models.DecimalField(decimal_places=2, max_digits=8)),
                ("url", models.TextField()),
                ("description", models.TextField()),
                ("stock", models.PositiveIntegerField()),
            ],
        ),
    ]
