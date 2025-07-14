from django.urls import path

from .views import home, shop

app_name = "core"

urlpatterns = [
    path('', home, name="home"),
    path('shop/', shop, name="shop")
]