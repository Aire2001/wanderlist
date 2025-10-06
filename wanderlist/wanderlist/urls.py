from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("accounts.urls")),
]
urlpatterns = [
    path("admin/", admin.site.urls),          # Django admin panel
    path("", include("accounts.urls")),       # All app routes (home, login, CRUD, etc.)
]

