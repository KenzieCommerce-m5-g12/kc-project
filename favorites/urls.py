from django.urls import path
from . import views

urlpatterns = [
    path("favorites/", views.FavoritesView.as_view()),
    path("favorites/user/", views.FavoritesListView.as_view()),
    path("favorites/<int:pk>/", views.FavoritesDetailView.as_view()),
]
