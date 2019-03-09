from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('executive/', views.home, name='home'),
    path('create-executive/', views.create_executive, name='create_executive'),
    # path('single-post/<post_id>/', views.single_post, name='single-post')
]