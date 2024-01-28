from django.shortcuts import render
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from .models import Agent

# Create your views here.


class NewAgent(CreateView):
    model = Agent
    fields = '__all__'


class ViewAgent(ListView):
    model = Agent
    context_object_name = 'Agents'


class UpdateAgent(UpdateView):
    model = Agent
    fields = '__all__'


class DeleteAgent(DeleteView):
    model = Agent
    success_url = '/Form/new'
