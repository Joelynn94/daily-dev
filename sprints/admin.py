from django.contrib import admin
from .models import Sprint


@admin.register(Sprint)
class SprintAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'start_date', 'end_date')
