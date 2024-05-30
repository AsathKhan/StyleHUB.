from django.shortcuts import render, redirect
from .forms import ProductsForm
from .models import Products

# Create your views here.
def homepage(request):
    return render(request, 'homepage1.html')

def products(request):
    obj=ProductsForm()
    if request.method == "POST":
        mydata=ProductsForm(request.POST)
        
        if mydata.is_valid:
            mydata.save()
    return render(request, 'product.html', {'data':obj})

def ptable(request):
    mydata=Products.objects.all()
    return render(request, 'producttable1.html',{'data':mydata})

def delete(request, id):
    mydata=Products.objects.get(id=id)
    mydata.delete()
    return redirect('catlogurl')

def update(request,id):
    mydata=Products.objects.get(id=id)
    form_template=ProductsForm(instance=mydata)
    if request.method == "POST":
        mydata=ProductsForm(request.POST, instance=mydata)
        
        if mydata.is_valid:
            mydata.save()
            return redirect("catlogurl")
    return render(request, 'product.html', {'data':form_template})

def employee(request):
    return render(request, 'employee.html')

def about(request):
    return render(request, 'about1.html')