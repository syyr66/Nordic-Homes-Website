import re
from django.contrib.auth import get_user_model
from django.db import models
from django.core.exceptions import ValidationError

from products.models import Product


def validate_phone_number(num):
    phone = str(num)
    if not re.fullmatch(r'\+?\d+', phone):
        raise ValidationError("Phone number shouldn't contain any characters except numbers and an optional leading '+'.")



class Order(models.Model):
    ORDERED = 'ordered'
    SHIPPED = 'shipped'

    STATUS_CHOICES = [
        (ORDERED, 'Ordered'),
        (SHIPPED, 'Shipped')
    ]

    user = models.ForeignKey(get_user_model(), related_name="orders", blank=True, null=True, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)

    address = models.CharField(max_length=255)
    zipcode = models.PositiveIntegerField()
    city = models.CharField(max_length=255)
    phone = models.CharField(max_length=30, validators=[validate_phone_number])
    
    created_at = models.DateTimeField(auto_now_add=True)
    paid = models.BooleanField(default=False)
    paid_amount = models.IntegerField(blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default=ORDERED)

    def get_total_price(self):
        return sum(item.price for item in self.items.all())

class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name="items", on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='items', on_delete=models.CASCADE)
    price = models.PositiveIntegerField()
    quantity = models.PositiveIntegerField(default=1)
