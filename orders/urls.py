from django.urls import path
from .views import OrderListCreateView, OrderRetrieveUpdateView

urlpatterns = [
    path("orders/", OrderListCreateView.as_view(), name="order-list-create"),
    path(
        "orders/<int:pk>/",
        OrderRetrieveUpdateView.as_view(),
        name="order-retrieve-update",
    ),
]
