from django.contrib.auth import login, get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.db.models import Q
from django.shortcuts import render, redirect
from django.views.generic import CreateView

from products.models import Product, Category

from .forms import SignUpForm, LogInForm


def home(request):
    products = Product.objects.all()[:8]

    return render(request, "core/home.html", {
        'products': products,
        'title': 'Home'
    })


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
        'title': 'Shopping',
        'products': products,
        'categories': categories,
        'active_category': active_category,
    }        

    return render(request, "core/shop.html", context)
        

def signup_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)

        if form.is_valid():
            user = form.save()

            login(request, user)

            return redirect('/')
    else:
        form = SignUpForm()

    return render(request, "core/signup.html", {
        "form": form, 
        "title": 'Sign up',
    })


class LoginUser(LoginView):
    template_name = "core/login.html"
    authentication_form = LogInForm
    extra_context = {
        'title': 'Log in',
    }


@login_required
def myaccount(request):
    return render(request, 'core/myaccount.html')


@login_required
def edit_account(request):
    return render(request, 'core/edit_account.html')


