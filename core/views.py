from django.shortcuts import render

from products.models import Product, Category


def home(request):
    products = Product.objects.all()[:8]

    return render(request, "core/home.html", {'products': products})


def shop(request):
    products = Product.objects.all()[:8]
    categories = Category.objects.all()

    return render(request, "core/shop.html", {
        'products': products,
        'categories': categories
    })
        