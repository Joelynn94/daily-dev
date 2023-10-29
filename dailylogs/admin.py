from django.contrib import admin
from .models import DailyLog


@admin.register(DailyLog)
class DailyLogAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'date', 'user')
