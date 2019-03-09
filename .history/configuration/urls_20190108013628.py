from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', include('App_Name.urls'), name='home'),
]
