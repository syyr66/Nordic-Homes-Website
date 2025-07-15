from django.urls import path

from products.views import product_detail

app_name = "products"

urlpatterns = [
    path('<slug:slug>', product_detail, name="product_detail"),
]