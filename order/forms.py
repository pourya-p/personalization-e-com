import re

from django import forms
from django.core.exceptions import ValidationError
from .models import Order




class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ["name", "phone_number", "address"]

    def clean_phone_number(self):
        phone_number = self.cleaned_data['phone_number']
        pattern = re.compile(r"^0?9\d{9}$")
        if not pattern.match(phone_number):
            raise ValidationError('تلفن صحیح نیست')
