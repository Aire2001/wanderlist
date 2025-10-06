from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("profile/", views.profile_view, name="profile"),

    # Auth
    path("register/", views.register_view, name="register"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),

    # Destinations
    path("destinations/", views.destination_list, name="destination_list"),
    path("destinations/add/", views.destination_create, name="destination_create"),
    path("destinations/<int:pk>/edit/", views.destination_update, name="destination_update"),
    path("destinations/<int:pk>/delete/", views.destination_delete, name="destination_delete"),
]
