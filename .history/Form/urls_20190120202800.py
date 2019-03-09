from django.urls import path
from . import views

urlpatterns = [
    path('executive/', views.form_1, name='form'),


]
