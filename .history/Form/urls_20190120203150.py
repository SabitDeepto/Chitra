from django.urls import path
from . import views

urlpatterns = [
    path('profile', views.form_1, name='form'),

]
