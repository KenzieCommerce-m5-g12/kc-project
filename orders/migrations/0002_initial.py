# Generated by Django 4.2.2 on 2023-07-04 15:37

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("products", "0001_initial"),
        ("orders", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="orders",
            name="products",
            field=models.ManyToManyField(related_name="orders", to="products.product"),
        ),
    ]
