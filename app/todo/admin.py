from django.contrib import admin

from .models import Todo


@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
    list_display = ('pk', 'user', 'title', 'important', 'memo', 'date_completed')
    readonly_fields = ('created',)
