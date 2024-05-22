from django import forms
from products.models import *


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['username', 'phone', 'email', 'quantity', 'product']