from django.shortcuts import render, redirect
from .models import ToDoTask
from .forms import TaskForm
from datetime import datetime

def home(request):

    todotasks = ToDoTask.objects.all()

    form = TaskForm()

    current_date = datetime.now()

    if request.method == 'POST':
        if 'save' in request.POST:
            pk = request.POST.get('save')
            if not pk:
                form = TaskForm(request.POST)
            else:
                task_to_modify = ToDoTask.objects.get(id = pk)
                form = TaskForm(request.POST, instance = task_to_modify)
            form.save()
            form = TaskForm()
        elif 'delete' in request.POST:
            pk = request.POST.get('delete')
            task_to_modify = ToDoTask.objects.get(id = pk)
            task_to_modify.delete()
        elif 'edit' in request.POST:
            pk = request.POST.get('edit')
            task_to_modify = ToDoTask.objects.get(id = pk)
            form = TaskForm(instance = task_to_modify)

    context = {
        'todotasks' : todotasks,
        'form' : form,
        'current_date' : current_date,
        'title' : 'Home',
    }

    return render(request, 'task/home.html', context)