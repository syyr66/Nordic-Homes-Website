from django.urls import path
from django.contrib.auth.views import LogoutView

from . import views

app_name = "core"

urlpatterns = [
    path('', views.home, name="home"),
    path('shop/', views.shop, name="shop"),
    path('signup/', views.signup_user, name="signup_user"),
    path('login/', views.LoginUser.as_view(), name="login_user"),
    path('logout/', LogoutView.as_view(), name="logout_user"),
    path('myaccount/', views.myaccount, name="my_account")
]