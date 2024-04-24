from django import forms
from .models import ToDoTask

class TaskForm(forms.ModelForm):
    class Meta:
        model = ToDoTask
        fields = ['start_by', 'end_by', 'task', 'note', 'status']