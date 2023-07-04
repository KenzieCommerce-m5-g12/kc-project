from django.urls import path
from . import views

urlpatterns = [
    path("carts/", views.CartView.as_view()),
    path("carts/<int:pk>/", views.CartDetailView.as_view()),
]
