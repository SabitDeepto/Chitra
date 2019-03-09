from django.contrib import admin

# Register your models here.
from .models import Profile


class MyAdmin(admin.ModelAdmin):
    list_display = ['user', 'bio', 'location', '']
admin.site.register(Profile, MyAdmin)