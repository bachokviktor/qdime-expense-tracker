from django.urls import path

from . import views

app_name = "users"

urlpatterns = [
    path("profile/", views.ProfileView.as_view(), name="profile"),
    path("login/", views.LoginView.as_view(), name="login"),
    path("registration/", views.RegistrationView.as_view(), name="registration"),
    path("logout/", views.LogoutView.as_view(), name="logout")
]
