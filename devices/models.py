from django.db import models


class Device(models.Model):
    name = models.CharField(max_length=120)
    created = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)
