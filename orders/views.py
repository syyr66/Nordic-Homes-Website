from django.shortcuts import render, redirect

from .forms import OrderForm
from .models import Order, OrderItem
from cart.cart import Cart


def start_order(request):
    cart = Cart(request)
    
    if request.method == 'POST':
        form = OrderForm(request.POST)

        if form.is_valid():
            order = form.save(commit=False)
            order.user = request.user
            order.save()
        
            for item in cart:
                product = item['product']
                quantity = item['quantity']
                price = product.price * quantity

                item = OrderItem.objects.create(order=order, product=product, price=price, quantity=quantity)

            cart.clear()

            return redirect('core:my_account')

        else:
            return render(request, "cart/checkout.html", {'title' : 'Checkout', 'form': form})

    return redirect('cart:cart')



        