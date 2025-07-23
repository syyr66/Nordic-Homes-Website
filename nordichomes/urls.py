from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("core.urls", namespace="core")),
    path('', include("cart.urls", namespace="cart")),
    path('products/', include("products.urls", namespace="products")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
