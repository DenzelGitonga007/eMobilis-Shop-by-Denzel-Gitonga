# forms.py
from django import forms
from .models import Product

# Create product
class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'


# Product edit form
class ProductEditForm(forms.ModelForm):    
    class Meta:
        model = Product
        fields = ['name', 'price', 'description']
