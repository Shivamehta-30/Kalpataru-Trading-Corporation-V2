from django.db import models
from django.urls import reverse


class Transport(models.Model):
    transport_name = models.CharField(max_length=150)

    def __str__(self):
        return self.transport_name

    def get_absolute_url(self):
        return reverse("Form-new")
