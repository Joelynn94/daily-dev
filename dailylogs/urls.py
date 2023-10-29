from django.urls import path
from .views import dailylog_list

urlpatterns = [
    path('/', dailylog_list, name='dailylog_list'),
]
