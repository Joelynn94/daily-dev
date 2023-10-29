from django.db import models
from django.contrib.auth.models import User


class Project(models.Model):
    statuses = [
        ('New', 'New'),
        ('In Progress', 'In Progress'),
        ('Completed', 'Completed'),
        ('Archived', 'Archived'),
    ]
    title = models.CharField(max_length=200)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    due_date = models.DateTimeField(blank=True, null=True)
    status = models.CharField(max_length=200, default='New', choices=statuses)
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
