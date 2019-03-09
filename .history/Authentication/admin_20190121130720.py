from django.contrib import admin

# Register your models here.
from .models import Profile


class MyAdmin(admin.ModelAdmin):
    list_display = ['user', 'bio']
admin.site.register(Profile, MyAdmin)