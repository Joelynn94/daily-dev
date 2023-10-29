from django.shortcuts import render
from .models import DailyLog


def dailylog_list(request):
    dailylogs = DailyLog.objects.all()
    context = {'dailylogs': dailylogs}
    return render(request, 'dailylogs/dailylog_list.html', context)
