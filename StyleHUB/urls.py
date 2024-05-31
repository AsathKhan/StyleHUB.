from django.contrib import admin
from django.urls import path,include
from customerapp import views
from django.views.generic.base import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('customerapp.urls')),
    path('accounts/', include("django.contrib.auth.urls"), name = "loginurl"),

]
