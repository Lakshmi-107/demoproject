from django import forms

from home.models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form_control', 'placeholder': "Name of the product"}),
            'price': forms.NumberInput(attrs={'class': 'form_control', 'placeholder': "Name of the product"}),
            'description': forms.TextInput(attrs={'class': 'form_control', 'placeholder': "Name of the product"}),
            'category': forms.TextInput(attrs={'class': 'form_control', 'placeholder': "Name of the product"}),
            'image': forms.TextInput(attrs={'class': 'form_control', 'placeholder': "Name of the product"}),
            'available': forms.TextInput(attrs={'class': 'form_control', 'placeholder': "Name of the product"}),
            'stock': forms.TextInput(attrs={'class': 'form_control', 'placeholder': "Name of the product"}),
        }
