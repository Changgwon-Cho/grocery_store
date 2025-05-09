from django import forms
from .models import Basket

class BasketAddForm(forms.ModelForm):
    class Meta:
        model = Basket
        fields = ['product', 'quantity']
        widgets = {
            'product': forms.Select(attrs={'class': 'form-select'}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control', 'min': 1}),
        }