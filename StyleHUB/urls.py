from django.contrib import admin
from django.urls import path,include
from customerapp import views
from django.views.generic.base import TemplateView
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('customerapp.urls')),
    path('accounts/', include("django.contrib.auth.urls"), name = "loginurl"),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
