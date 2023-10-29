from django.shortcuts import render
from .models import Sprint


def sprint_list(request):
    sprints = Sprint.objects.all()
    context = {'sprints': sprints}
    return render(request, 'sprints/sprint_list.html', context)
