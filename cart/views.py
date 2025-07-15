from django.shortcuts import render

from .cart import Cart


def add_to_cart(request, product_id):
    cart = Cart(request)
    product_id_str = str(product_id)
    
    if product_id_str in cart.cart and cart.cart[product_id_str]['quantity'] >= 1:
        cart.add(product_id, update_quantity=True)
    else:
        cart.add(product_id)

    return render(request, 'cart/menu_cart.html')