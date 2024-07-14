from django import forms
from django.core.exceptions import ValidationError
import re

class OrderForm(forms.Form):
    id = forms.CharField(max_length=100)
    name = forms.CharField(max_length=100)
    city = forms.CharField(max_length=100)
    district = forms.CharField(max_length=100)
    street = forms.CharField(max_length=100)
    price = forms.DecimalField(max_digits=10, decimal_places=2)
    currency = forms.CharField(max_length=100)
    
    def clean_name(self):
        name = self.cleaned_data["name"]
        if not re.match(r"^[A-Za-z ]+$", name):
            raise ValidationError("Name contains non-English characters")
        if not name[0].isupper():
            raise ValidationError("Name is not capitalized")
        return name
            
    def clean_price(self):
        price = self.cleaned_data["price"]
        if price > 2000:
            raise ValidationError("Price is over 2000")
        return price
        
    def clean_currency(self):
        currency = self.cleaned_data["currency"]
        if currency not in ["TWD", "USD"]:
            raise ValidationError("Currency format is wrong")
        return currency