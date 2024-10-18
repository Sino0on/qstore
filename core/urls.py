from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin


urlpatterns = [
    path("api/v1/", include("api.router")),
    path('dev-admin8/', admin.site.urls),
    path("docs/", include("api.openapi.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)