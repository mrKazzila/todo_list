from django.contrib import admin

from .models import Todo


@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
    """Register the Todo model and settings fields for admin"""  # skip

    list_display = ('pk', 'user', 'title', 'important', 'memo', 'date_completed')
    readonly_fields = ('created',)
