from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    due_date = models.DateTimeField(blank=True, null=True)
    creator = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='created_projects', null=True, blank=True)

    def __str__(self):
        return self.title


class ProjectMembership(models.Model):
    roles = [
        ('Member', 'Member'),
        ('Developer', 'Developer'),
        ('Designer', 'Designer'),
        ('Project Manager', 'Project Manager'),
        ('QA', 'QA'),
        ('HR', 'HR'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    role = models.CharField(max_length=100, choices=roles,
                            default='Member', null=True, blank=True)

    def __str__(self):
        return f"{self.user.username} in {self.project.title}"


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


class Sprint(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    start_date = models.DateTimeField(default=None, blank=True, null=True)
    end_date = models.DateTimeField(default=None, blank=True, null=True)
    tasks = models.ManyToManyField(Task, blank=True, related_name='sprints')

    def __str__(self):
        return self.title


class DailyLog(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    tasks = models.ManyToManyField(Task, blank=True, related_name='daily_logs')
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
