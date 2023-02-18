from django.contrib import admin

from todo.models import Todo


@admin.register(Todo)
class UserAdmin(admin.ModelAdmin):
    list_display = ('user', 'title', 'important', 'memo', 'date_completed',)
    readonly_fields = ('created', )
