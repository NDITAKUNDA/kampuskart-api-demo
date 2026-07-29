from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/products/", include("products.urls")),
]

handler404 = "kampuskart.views.custom_404"
handler500 = "kampuskart.views.custom_500"
