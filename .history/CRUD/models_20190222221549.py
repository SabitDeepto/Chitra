from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.


class Executive(models.Model):
    name = models.CharField(max_length=200)
    is_executive = models.BooleanField(default=True)
    registration_date = models.DateTimeField(default=timezone.now)
    educational_institue = models.CharField(max_length=210)
    hsc_year = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class PaymentRequest(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    last_3_digit = models.IntegerField(null=True)
    transaction_id = models.IntegerField(null=True)
    date = models.DateTimeField(auto_now_add=True)
    gender_choice = (
        ('done', 'DONE'),
        ('pending', 'PENDING'),
    )
    status = models.CharField(choices=gender_choice, max_length=200)
