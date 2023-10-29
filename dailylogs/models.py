from django.db import models
from django.contrib.auth.models import User
from tasks.models import Task


class DailyLog(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    tasks = models.ManyToManyField(Task, blank=True, related_name='daily_logs')
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
