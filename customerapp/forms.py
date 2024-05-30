from django import forms
from .models import Products

class ProductsForm(forms.ModelForm):
    class Meta:
        model=Products
        fields='__all__'
        
        widgets={
            'Gender': forms.RadioSelect,
        }
        
        labels = {
            'Product_Name': 'Name',
            'Product_Code': 'Code',
            'Fabric_Type': 'Type',          
            
        }
        