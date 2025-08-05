from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from django.contrib.auth.decorators import login_required
from .models import Task


@login_required
def task_list(request):
    tasks = Task.objects.all()
    context = {'tasks': tasks}
    return render(request, 'tasks/task_list.html', context)


@login_required
def task_detail(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    context = {'task': task}
    return render(request, 'tasks/task_detail.html', context)
