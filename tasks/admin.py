from django.contrib import admin
from .models import Tag, Comment, Task


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('text',)


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'status',
                    'priority', 'created_at', 'due_date', 'project')
    list_filter = ('status', 'priority', 'project')
