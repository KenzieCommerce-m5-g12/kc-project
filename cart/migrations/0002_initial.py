# Generated by Django 4.2.3 on 2023-07-06 21:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("products", "0001_initial"),
        ("cart", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="cartproduct",
            name="product",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="product_data",
                to="products.product",
            ),
        ),
        migrations.AddField(
            model_name="cart",
            name="products_cart",
            field=models.ManyToManyField(
                related_name="cart_products",
                through="cart.CartProduct",
                to="products.product",
            ),
        ),
    ]
