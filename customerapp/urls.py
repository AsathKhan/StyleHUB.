from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.homepage, name="homepageurl"),
    path('CatalogList/Addproducts', views.products, name="addproductsurl"),
    path('CatalogList', views.ptable, name="catlogurl"),
    path('Update/<int:id>',views.update, name= "updateurl"),
    path('Delete/<int:id>', views.delete, name= "deleteurl"),
    path('employee',views.employee, name = 'employeeurl'),
    path('About', views.about, name='abouturl'),
    path('CatalogTable', views.ptable, name="catloggurl"),   
    path('Catalog', views.viewproducts, name = "viewproductsurl"),
]
