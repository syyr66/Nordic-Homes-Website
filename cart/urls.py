from django.urls import path

from . import views

app_name = "cart"

urlpatterns = [
    path('add_to_cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/', views.cart, name='cart'),
    path('cart/checkout/', views.checkout, name="checkout"),
]