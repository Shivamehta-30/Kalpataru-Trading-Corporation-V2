from django.shortcuts import render
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from .models import Transport

# Create your views here.


class NewTransport(CreateView):
    model = Transport
    fields = '__all__'


class ViewTransport(ListView):
    model = Transport
    context_object_name = 'Transports'


class UpdateTransport(UpdateView):
    model = Transport
    fields = '__all__'


class DeleteTransport(DeleteView):
    model = Transport
    success_url = '/Form/new'
