from django.shortcuts import render
from .models import DailyLog


def dailylog_list(request):
    dailylogs = DailyLog.objects.all()
    context = {'dailylogs': dailylogs}
    return render(request, 'projects/dailylog_list.html', context)
