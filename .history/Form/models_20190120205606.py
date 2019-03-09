from django.db import models


class Profile_1(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)

    class Meta:
        verbose_name_plural = "profile_1"

    def __str__(self):
        return self.first_name