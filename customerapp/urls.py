from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.homepage, name="homepageurl"),
    path('Catlog/addproducts', views.products, name="addproductsurl"),
    path('Catlog', views.ptable, name="catlogurl"),
    path('Update/<int:id>',views.update, name= "updateurl"),
    path('Delete/<int:id>', views.delete, name= "deleteurl"),
    path('employee',views.employee, name = 'employeeurl'),
    path('About', views.about, name='abouturl'),
    path('Catlogg', views.ptable, name="catloggurl"),   
    path('productview', views.productview, name = "productviewurl"),
]
