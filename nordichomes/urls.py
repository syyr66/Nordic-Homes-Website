from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("core.urls", namespace="core")),
    path('', include("cart.urls", namespace="cart")),
    path('products/', include("products.urls", namespace="products")),
]
