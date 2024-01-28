from django.db import models
from django.urls import reverse


class Seller(models.Model):
    seller_name = models.CharField(max_length=150)

    def __str__(self):
        return self.seller_name

    def get_absolute_url(self):
        return reverse("Form-new")
