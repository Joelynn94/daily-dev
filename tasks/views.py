from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from .models import Task


def task_list(request):
    tasks = Task.objects.all()
    context = {'tasks': tasks}
    return render(request, 'tasks/task_list.html', context)

def task_detail(request, task_id):
    task = Task.objects.get(task_id=task_id)
    context = {'task': task}
    return render(request, 'tasls/task_detail.html', context)
