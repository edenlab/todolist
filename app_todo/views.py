from django.shortcuts import render, redirect, get_object_or_404
from django.forms import ModelForm

from .models import Task

# Create your views here.

class TaskForm(ModelForm):
  class Meta:
    model = Task
    fields = ['description', 'due_date']

def home(request, template_name='app_todo/home.html'):
  tasks = Task.objects.all()
  ctx = {}
  ctx['tasks'] = tasks
  return render(request, template_name, ctx)

def task_create(request, template_name='app_todo/task_form.html'):
  form = TaskForm(request.POST or None)
  if form.is_valid():
    form.save()
    return redirect('app_todo:home')
  ctx = {}
  ctx['form'] = form
  return render(request, template_name, ctx)

def task_update(request, id, template_name='app_todo/task_form.html'):
  task = get_object_or_404(Task, id=id)
  form = TaskForm(request.POST or None, instance=task)
  if form.is_valid():
    form.save()
    return redirect('app_todo:home')
  ctx = {}
  ctx['form'] = form
  ctx['task'] = task
  return render(request, template_name, ctx)

def task_delete(request, id, template_name='app_todo/task_confirm_delete.html'):
  task = get_object_or_404(Task, id=id)
  if request.method=='POST':
    task.delete()
    return redirect('app_todo:home')
  ctx = {}
  ctx['task'] = task
  return render(request, template_name, ctx)

