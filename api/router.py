from django.urls import path, include


urlpatterns = [
    path("product/", include("api.product.urls")),
    path("authentication/", include("api.authentication.urls")),
    path("cabinet/", include("api.user_cabinet.urls")),
    path("docs/", include("api.openapi.urls")),
]
