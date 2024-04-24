from django.contrib import admin
from .models import ToDoTask

class AdminModel(admin.ModelAdmin):
    list_display = ['task', 'note', 'start_by', 'end_by', 'status']

admin.site.register(ToDoTask, AdminModel)