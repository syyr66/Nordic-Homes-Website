from django.db.models import Q
from django.shortcuts import render

from products.models import Product, Category


def home(request):
    products = Product.objects.all()[:8]

    return render(request, "core/home.html", {'products': products})


def shop(request):
    active_category = request.GET.get('category', '')
    query = request.GET.get('query', '')

    categories = Category.objects.all() 

    if active_category:
        products = Product.objects.filter(category__slug=active_category)
    else:
        products = Product.objects.all()
    
    if query:
        products = products.filter(Q(name__icontains=query) | Q(description__icontains=query))


    context = {
        'products': products,
        'categories': categories,
        'active_category': active_category,
    }        

    return render(request, "core/shop.html", context)
        

def signup(request):
    return render(request, "core/signup.html")

def login(request):
    return render(request, "core/login.html")