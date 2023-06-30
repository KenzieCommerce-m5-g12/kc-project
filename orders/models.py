from django.db import models


class StatusChoices(models.TextChoices):
    PEDIDO_REALIZADO = "Pedido realizado"
    EM_ANDAMENTO = "Em andamento"
    ENTREGUE = "Entregue"


class Orders(models.Model):
    status = models.CharField(
        max_length=25, choices=StatusChoices.choices, default=StatusChoices.EM_ANDAMENTO
    )
    products = models.ManyToManyField("products.Product", related_name="orders")
    user = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name="orders"
    )
    createdAt = models.DateTimeField(auto_now_add=True)
