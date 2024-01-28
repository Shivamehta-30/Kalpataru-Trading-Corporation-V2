from django.shortcuts import render
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from .models import Buyer

# Create your views here.


class NewBuyer(CreateView):
    model = Buyer
    fields = '__all__'


class ViewBuyer(ListView):
    model = Buyer
    context_object_name = 'Buyers'


class UpdateBuyer(UpdateView):
    model = Buyer
    fields = '__all__'


class DeleteBuyer(DeleteView):
    model = Buyer
    success_url = '/Form/new'
