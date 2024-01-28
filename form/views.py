from django.shortcuts import render
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from .forms import FormModelForm
from .models import Form
from django.urls import reverse
# Create your views here.


class NewForm(CreateView):
    model = Form
    form_class = FormModelForm
    


class ViewForm(ListView):
    model = Form
    context_object_name = 'Forms'


class UpdateForm(UpdateView):
    model = Form
    fields = '__all__'
    success_url = '/view'


class DeleteForm(DeleteView):
    model = Form
    success_url = '/view'


def download(request, id):
    object = Form.objects.get(id=id)
    return render(request, "form/form_print.html", {
        "object": object
    })



