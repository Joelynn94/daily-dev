from django.contrib import admin
from .models import Project, Tag, Comment, Task, Sprint, DailyLog


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'created_at', 'due_date')


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('text',)


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'status', 'priority', 'created_at', 'due_date', 'project')
    list_filter = ('status', 'priority', 'project')


@admin.register(Sprint)
class SprintAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'start_date', 'end_date')


@admin.register(DailyLog)
class DailyLogAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'date', 'user')