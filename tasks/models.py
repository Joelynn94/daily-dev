from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from projects.models import Project


class Tag(models.Model):
    name = models.CharField(max_length=100)
    color = models.CharField(max_length=7, blank=True, null=True)

    def __str__(self):
        return self.name


class Comment(models.Model):
    text = models.TextField()
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='comments', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text


class Task(models.Model):
    PRIORITY_CHOICES = [
        ('Low', 'Low'),
        ('Medium', 'Medium'),
        ('High', 'High'),
    ]
    STATUS_CHOICES = [
        ('New', 'New'),
        ('Backlog', 'Backlog'),
        ('To Do', 'To Do'),
        ('In Review', 'In Review'),
        ('In Progress', 'In Progress'),
        ('Completed', 'Completed'),
        ('Archived', 'Archived'),
    ]
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    status = models.CharField(
        max_length=200, choices=STATUS_CHOICES, default='New')
    priority = models.CharField(
        max_length=200, choices=PRIORITY_CHOICES, default='Low', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    due_date = models.DateTimeField(blank=True, null=True)
    tags = models.ManyToManyField('Tag', blank=True)
    comments = models.ManyToManyField('Comment', blank=True)
    assignee = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, blank=True, related_name='assigned_tasks')
    project = models.ForeignKey(
        Project, on_delete=models.CASCADE, related_name='tasks', null=True, blank=True)

    def __str__(self):
        return self.title
