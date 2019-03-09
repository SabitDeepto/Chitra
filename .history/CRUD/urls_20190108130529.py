from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('executive/', views.home, name='home'),
    path('create/', views.create_executive, name='create_executive'),
    path('update/<int:id>', views.update_executive, name='update_executive'),

]
