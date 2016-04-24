from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView,ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView


# Create your views here.
class ListTask(ListView):
  tasks = Task.objects.all()

class NewTask(CreateView):
  model = Task
