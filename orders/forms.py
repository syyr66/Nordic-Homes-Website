from django import forms

from .models import Order

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'email', 'address', 'zipcode', 'city', 'phone']
        labels = {
            'first_name': 'First Name',
            'last_name': 'Last Name', 
            'email': 'Email',
            'address': 'Address', 
            'zipcode': 'Zipcode',
            'phone': 'Phone'
        }