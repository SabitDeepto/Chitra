from django.contrib import admin
from .models import Profile_1, Profile_2, PaymentRequest

# Register your models here.


class MyCustomAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name']

admin.site.register(Profile_1, MyCustomAdmin)


class Profile_2_Admin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'gender']
admin.site.register(Profile_2, Profile_2_Admin)
