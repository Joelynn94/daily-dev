from django.db import models
from tasks.models import Task


class Sprint(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    start_date = models.DateTimeField(default=None, blank=True, null=True)
    end_date = models.DateTimeField(default=None, blank=True, null=True)
    tasks = models.ManyToManyField(Task, blank=True, related_name='sprints')

    def __str__(self):
        return self.title
