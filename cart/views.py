from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from .cart import Cart


def add_to_cart(request, product_id):
    cart = Cart(request)
    product_id_str = str(product_id)
    
    if product_id_str in cart.cart and cart.cart[product_id_str]['quantity'] >= 1:
        cart.add(product_id, update_quantity=True)
    else:
        cart.add(product_id)

    return render(request, 'cart/menu_cart.html')


def cart(request):
    return render(request, 'cart/cart.html', {
        'title' : 'Cart overview',
        'next_page': reverse('cart:checkout'),
    })

@login_required(login_url="/login/")
def checkout(request):
    return render(request, "cart/checkout.html", {
        'title' : 'Checkout',
        'next_page': reverse('core:home'), #Home page because i don't have order_detail view yet
    })