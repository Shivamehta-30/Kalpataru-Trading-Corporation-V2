from django.shortcuts import render
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from .models import Seller

# Create your views here.


class NewSeller(CreateView):
    model = Seller
    fields = '__all__'


class ViewSeller(ListView):
    model = Seller
    context_object_name = 'Sellers'


class UpdateSeller(UpdateView):
    model = Seller
    fields = '__all__'


class DeleteSeller(DeleteView):
    model = Seller
    success_url = '/Form/new'
