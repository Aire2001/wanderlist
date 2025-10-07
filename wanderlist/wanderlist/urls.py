from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # ============================
    # ⚙️ ADMIN & APP ROUTES
    # ============================
    path("admin/", admin.site.urls),           # Django Admin Panel
    path("", include("accounts.urls")),        # All routes from the 'accounts' app
]

# ============================
# 🖼️ MEDIA FILE HANDLING (for profile pictures)
# ============================
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
