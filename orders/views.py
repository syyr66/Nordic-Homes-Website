import stripe
from django.conf import settings
from django.http import JsonResponse
from django.shortcuts import render, redirect

from .forms import OrderForm
from .models import Order, OrderItem
from cart.cart import Cart


def start_order(request):
    cart = Cart(request)

    if not cart.cart:
        return redirect('core:home')

    total_price = 0
    
    if request.method == 'POST':
        form = OrderForm(request.POST)

        if form.is_valid():
            order = form.save(commit=False)
            order.user = request.user
            order.save()
            print(order.id)

            line_items = []
            for item in cart:
                product = item['product']
                quantity = item['quantity']
                price = product.price * quantity
                total_price += price

                item = OrderItem.objects.create(
                    order=order,
                    product=product,
                    price=price,
                    quantity=quantity
                )

                line_items.append({
                    'price_data': {
                        'currency': 'usd',
                        'product_data': {
                            'name': product.name,
                        },
                        'unit_amount': int(product.price * 100),
                    },
                    'quantity': quantity,
                })

            cart.clear()

            stripe.api_key = settings.STRIPE_API_KEY_HIDDEN

            try:
                session = stripe.checkout.Session.create(
                    payment_method_types=['card'],
                    line_items=line_items,
                    mode='payment',
                    success_url=request.build_absolute_uri('/payment/success/?session_id={CHECKOUT_SESSION_ID}'),
                    cancel_url=request.build_absolute_uri('/cart/'),
            )
            except error as e:
                return render(request, 'cart/checkout.html', {
                    'form': form,
                    'error': str(e),
                })

            order.payment_intent = session.payment_intent
            order.paid_amount = total_price 
            order.save()

            return redirect(session.url)

        else:
            return render(request, 'cart/checkout.html', {
                'form': form,
            })

    return redirect('core:home')
