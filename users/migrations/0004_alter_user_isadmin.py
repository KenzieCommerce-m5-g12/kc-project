# Generated by Django 4.2.2 on 2023-07-03 16:39

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0003_user_address"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="isAdmin",
            field=models.BooleanField(default=False),
        ),
    ]
