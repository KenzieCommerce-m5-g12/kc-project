# Generated by Django 4.2.3 on 2023-07-07 11:58

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("orders", "0001_initial"),
        ("products", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="orders",
            name="products",
            field=models.ManyToManyField(related_name="orders", to="products.product"),
        ),
    ]
