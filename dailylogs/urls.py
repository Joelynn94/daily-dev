from django.urls import path
from .views import dailylog_list

urlpatterns = [
    path('logs/', dailylog_list, name='dailylog_list'),
]
