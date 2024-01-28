from django.shortcuts import render
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from .models import Quality

# Create your views here.


class NewQuality(CreateView):
    model = Quality
    fields = '__all__'


class ViewQuality(ListView):
    model = Quality
    context_object_name = 'Qualities'


class UpdateQuality(UpdateView):
    model = Quality
    fields = '__all__'


class DeleteQuality(DeleteView):
    model = Quality
    success_url = '/Form/new'
