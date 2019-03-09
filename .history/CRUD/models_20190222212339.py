from django.db import models
from django.utils import timezone
# Create your models here.


class Executive(models.Model):
    name = models.CharField(max_length=200)
    educational_institue = models.CharField(max_length=210)
    hsc_year = models.CharField(max_length=20)

    def __str__(self):
        return self.name