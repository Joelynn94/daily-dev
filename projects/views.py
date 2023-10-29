from django.shortcuts import render
from .models import Project


def project_list(request):
    projects = Project.objects.filter(creator=request.user)
    context = {'projects': projects}
    return render(request, 'projects/project_list.html', context)
