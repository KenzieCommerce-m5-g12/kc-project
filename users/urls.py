from django.urls import path
from users.views import UserView, UserDetailview

urlpatterns = [
    path("user/", UserView.as_view()),
    path("user/<int:user_id>/", UserDetailview.as_view())
]