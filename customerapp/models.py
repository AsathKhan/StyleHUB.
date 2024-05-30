from django.db import models

# Create your models here.
class Products(models.Model):
    biology=[
        ('M', 'Male'),
        ('F', 'Female'),
        ('U', 'Unisex'),
    ]
    
    types=[
        ('Natural', 'Natural'),
        ('Synthetic', 'Synthetic'),
        ('Semi-Synthetic', 'Semi-synthetic')
    ]
    
    Product_Name=models.CharField(max_length=50, blank=False)
    Brand=models.CharField(max_length=20)
    Product_Code=models.IntegerField(blank=False)
    Price=models.DecimalField(max_digits=10, decimal_places=2)
    Gender=models.CharField(choices=biology, max_length=8, blank=False)
    Fabric_Type=models.CharField(choices=types, max_length=25)
    Free_Size=models.BooleanField(default=False)
    
    