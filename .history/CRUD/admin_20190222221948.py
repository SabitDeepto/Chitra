from codecs import register

from django.contrib import admin

from CRUD.models import Executive


# Register your models here.
admin.site.register(Executive)


class PaymentRequest_Admin(admin.ModelAdmin):
    list_display = ['user', 'last_3_digit', 'transaction_id', 'date', 'status']
admin.site.register(PaymentRequest, PaymentRequest_Admin)