from django.contrib import admin
from django.urls import include, path
from Authentication.views import home


urlpatterns = [
    path('', views.home, name=home),
    path('admin/', admin.site.urls),
    path('', include('CRUD.urls'), name='home'),
    path('', include('Form.urls'), name='form'),
    path('', include('Authentication.urls'), name='authentication'),
]
