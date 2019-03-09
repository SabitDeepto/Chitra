from django.contrib import admin
from django.urls import include, path
from Authentication import views as h
from django.views.generic.base import TemplateView


urlpatterns = [
    path('', h.home),
    path('admin/', admin.site.urls),
    path('', include('CRUD.urls'), name='home'),
    path('', include('Form.urls'), name='form'),
    path('', include('Authentication.urls'), name='authentication'),


]
