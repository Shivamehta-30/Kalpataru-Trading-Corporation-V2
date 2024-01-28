from django.db import models
from django.urls import reverse


class Quality(models.Model):
    qun = models.CharField(max_length=150)

    def __str__(self):
        return self.qun

    def get_absolute_url(self):
        return reverse("Form-new")
