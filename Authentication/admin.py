from django.contrib import admin

# Register your models here.
from .models import Profile


class MyAdmin(admin.ModelAdmin):
    list_display = ['user', 'bio', 'location', 'birth_date']
admin.site.register(Profile, MyAdmin)