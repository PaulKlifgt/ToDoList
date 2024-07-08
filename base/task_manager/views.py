from django.shortcuts import get_object_or_404, render, redirect

from .models import Task
from .forms import TaskForm


def index(request):
    latest_tasks = Task.objects.order_by("done")
    context = {
        'latest_tasks': latest_tasks,
    }
    return render(request, 'task_manager/index.html', context)


def task(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    context={
        'task': task,
    }
    return render(request, 'task_manager/task.html', context)


def add(request):
    if request.method == 'POST':

        form = TaskForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('/')
        
    else:
        form = TaskForm()

    context={
        'form': form
    }
    
    return render(request, 'task_manager/add.html', context)


def done(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    task.done = True
    task.save()
    return redirect('/')


def undone(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    task.done = False
    task.save()
    return redirect('/')


def delete(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    task.delete()
    return redirect('/')


def change(request, task_id):
    if request.method == 'POST':
        task = get_object_or_404(Task, pk=task_id)
        form = TaskForm(request.POST, instance=task)
        
        if form.is_valid():
            task = form.save(commit=False)
            task.save()
            return redirect('/')
        
    else:
        form = TaskForm()

    context={
        'form': form,
    }
        
    return render(request, 'task_manager/change.html', context)


def error_404(request, exception):
    return render(request, 'task_manager/404.html', status=404)

def error_500(request, *args, **argv):
    return render(request, 'task_manager/500.html', status=404)