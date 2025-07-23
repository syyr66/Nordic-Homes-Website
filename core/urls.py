from django.urls import path

from . import views

app_name = "core"

urlpatterns = [
    path('', views.home, name="home"),
    path('shop/', views.shop, name="shop"),
    path('signup/', views.signup, name="signup"),
    path('login/', views.login, name="login"),
]