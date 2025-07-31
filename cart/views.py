from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from .cart import Cart
from products.models import Product


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


def update_cart(request, product_id, action):
    cart = Cart(request)

    if action == 'item_increment':
        cart.add(product_id, update_quantity=True)
    elif action == 'item_decrement':
        cart.add(product_id, quantity=-1, update_quantity=True)

    product = get_object_or_404(Product, id=product_id)

    try:
        quantity = cart.cart[str(product_id)]['quantity']
    except:
        response = HttpResponse('')
        response['HX-Trigger'] = 'update-menu-cart'
        return response

    item = {
        'product': product,
        'total_price': quantity * product.price,
        'quantity': quantity,
    }

    response = render(request, 'cart/partials/cart_item.html', {'item': item})
    response['HX-Trigger'] = 'update-menu-cart'

    return response


@login_required()
def checkout(request):
    return render(request, "cart/checkout.html", {
        'title' : 'Checkout',
    })


def hx_menu_cart(request):
    return render(request, 'cart/menu_cart.html')

def hx_summary(request):
    return render(request, 'cart/partials/summary.html', {'next_page': reverse('cart:checkout')})
    