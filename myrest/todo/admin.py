from django.contrib import admin
from .models import ToDoItem


@admin.register(ToDoItem)
class ToDoItemAdmin(admin.ModelAdmin):
    pass
    list_display = 'id', 'text', 'done'
