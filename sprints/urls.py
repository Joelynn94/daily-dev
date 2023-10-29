from django.urls import path
from .views import sprint_list

urlpatterns = [
    path('sprints/', sprint_list, name='sprint_list'),
]
