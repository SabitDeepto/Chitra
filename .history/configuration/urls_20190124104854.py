from django.contrib import admin
from django.urls import include, path
from Authentication import views as h
from Ajax import views
from django.views.generic.base import TemplateView


urlpatterns = [
    path('', h.home),
    path('admin/', admin.site.urls),
    path('', include('CRUD.urls'), name='home'),
    path('', include('Form.urls'), name='form'),
    path('', include('Authentication.urls'), name='authentication'),
    #ajax
    path('rooms/', TemplateView.as_view(template_name="rooms/main.html"), name='room_main'),
    path('rooms/list', views.RoomList.as_view(), name='room_list'),
    path('rooms/create', views.RoomCreate.as_view(), name='room_create'),
    path('rooms/update/<int:pk>', views.RoomUpdate.as_view(), name='room_update'),
    path('rooms/delete/<int:pk>', views.RoomDelete.as_view(), name='room_delete'),
    path('rooms/<int:pk>', views.RoomDetail.as_view(), name='room_detail'),

]
