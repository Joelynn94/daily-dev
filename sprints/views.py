from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Sprint

@login_required
def sprint_list(request):
    sprints = Sprint.objects.all()
    context = {'sprints': sprints}
    return render(request, 'sprints/sprint_list.html', context)
