from django.contrib import admin
from todo.models import Todo


class TodoAdmin(admin.ModelAdmin):
    list_display = ('id', 'description', 'status', 'lead_at')
    list_filter = ('id', 'description', 'status', 'lead_at')
    search_fields = ('description', 'status')
    fields = ('description', 'status', 'lead_at')


admin.site.register(Todo, TodoAdmin)

