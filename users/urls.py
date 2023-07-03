from django.urls import path
from users.views import UserView, UserDetailview, LoginView

urlpatterns = [
    path("users/", UserView.as_view()),
    path("users/<int:user_id>/", UserDetailview.as_view()),
    path("users/login/", LoginView.as_view())
]