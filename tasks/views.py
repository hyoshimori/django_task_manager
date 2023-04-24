from django.shortcuts import render, redirect, get_object_or_404
from .models import Task
from .forms import TaskForm

def list_tasks(request):
    tasks = Task.objects.all()
    return render(request, 'tasks/list_tasks.html', {'tasks': tasks})

def task_details(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    return render(request, 'tasks/task_details.html', {'task': task})

def create_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_tasks')
    else:
        form = TaskForm()
    return render(request, 'tasks/create_task.html', {'form': form})

def edit_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('list_tasks')
    else:
        form = TaskForm(instance=task)
    return render(request, 'tasks/edit_task.html', {'form': form, 'task': task})

def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    if request.method == 'POST':
        task.delete()
        return redirect('list_tasks')
    return render(request, 'tasks/delete_task.html', {'task': task})
