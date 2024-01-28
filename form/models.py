from django.db import models
from django.urls import reverse
from buyer_details.models import *
from seller_details.models import *
from quality.models import *
from agent.models import *
from transport.models import *


class Form(models.Model):
    date = models.DateField()
    sellername = models.ForeignKey(
        Seller, on_delete=models.CASCADE)
    buyername = models.ForeignKey(
        Buyer, on_delete=models.CASCADE)
    agentname = models.ForeignKey(
        Agent, on_delete=models.CASCADE)
    Quality = models.ForeignKey(
        Quality, on_delete=models.CASCADE)
    reed = models.CharField(max_length=150, null=True, blank=True)
    pik = models.CharField(max_length=150, null=True, blank=True)
    width = models.CharField(max_length=150, null=True, blank=True)
    pcs = models.CharField(max_length=150, null=True, blank=True)
    discount = models.CharField(max_length=150, null=True, blank=True)
    rate = models.CharField(max_length=150, null=True, blank=True)
    quantity = models.CharField(max_length=150, null=True, blank=True)
    delivery_period = models.CharField(max_length=150, null=True, blank=True)
    payment_terms = models.CharField(max_length=150,  null=True, blank=True)
    transport = models.ForeignKey(Transport, on_delete = models.CASCADE)
    delivery_at = models.CharField(max_length=150, null=True, blank=True)
    remarks = models.CharField(max_length=150, null=True, blank=True)

    def __str__(self):
        return f"{self.sellername} {self.buyername}"

    def get_absolute_url(self):
        success_url = reverse('download', kwargs={'id': self.pk})
        return success_url
