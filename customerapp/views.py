from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .forms import ProductsForm
from .models import Products

def homepage(request):
    return render(request, 'homepage1.html')

@login_required
def products(request):
    obj=ProductsForm()
    if request.method == "POST":
        mydata=ProductsForm(request.POST, request.FILES)
        
        if mydata.is_valid:
            mydata.save()
    return render(request, 'product.html', {'data':obj})

@login_required
def ptable(request):
    mydata=Products.objects.all()
    return render(request, 'producttable1.html',{'data':mydata})

@login_required
def delete(request, id):
    mydata=Products.objects.get(id=id)
    mydata.delete()
    return redirect('catlogurl')

@login_required
def update(request,id):
    mydata=Products.objects.get(id=id)
    form_template=ProductsForm(instance=mydata)
    if request.method == "POST":
        mydata=ProductsForm(request.POST, request.FILES, instance=mydata)
        
        if mydata.is_valid:
            mydata.save()
            return redirect("catlogurl")
    return render(request, 'product.html', {'data':form_template})

def employee(request):
    return render(request, 'employee.html')

def about(request):
    return render(request, 'about1.html')

def viewproducts(request):
    mydata=Products.objects.all()
    return render(request, 'productview1.html', {'data':mydata})