from .cart import Cart

def cart(request):
    return {'cart': Cart(request)}

def list_items_in_cart(request):
    cart = Cart(request)
    return [cart.cart[id]['product'] for id in cart.cart.keys()]