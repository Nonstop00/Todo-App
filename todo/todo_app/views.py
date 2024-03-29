from django.shortcuts import render , redirect
from django.http import HttpResponse

from .models import *
from .forms import *

def index(request):
    tasks = Task.objects.all()
    form = TaskForm()

    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')
    context = {'tasks': tasks,
               'form': form}
    return render(request,'todo_app/todo.html',context)

def taskUpdate(request, primaryKey):
    task = Task.objects.get(id=primaryKey)
    form = TaskForm(instance=task)

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('/')    
    
    context = {'form':form}
    return render(request,'todo_app/task_update.html',context)

def confirmDel(request,primaryKey):
    task = Task.objects.get(id=primaryKey)

    if request.method == 'POST':
        task.delete()
        return redirect('/')

    context ={'task':task}
    return render(request,'todo_app/confirm.html',context)