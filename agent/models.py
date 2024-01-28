from django.db import models
from django.urls import reverse


class Agent(models.Model):
    agent_name = models.CharField(max_length=150)

    def __str__(self):
        return self.agent_name

    def get_absolute_url(self):
        return reverse("Form-new")
