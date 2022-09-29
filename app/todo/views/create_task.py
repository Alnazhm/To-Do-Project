from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render, redirect, get_object_or_404
from todo.models import Todo, STATUS_OF_TASK


def add_view(request, *args, **kwargs):
    if request.method == 'GET':
        context = {
            'status_list': STATUS_OF_TASK
        }
        return render(request, 'create_task.html', context=context)

    task_data = {
        'description': request.POST.get('description'),
        'status': request.POST.get('status'),
        'lead_at': request.POST.get('lead_at'),
        'detail_description': request.POST.get('detail_description')
    }
    task = Todo.objects.create(**task_data)
    return redirect('task_detail', pk=task.pk)


def detail_view(request, pk):
    todo_task = get_object_or_404(Todo, pk=pk)
    return render(request, 'task.html', context={'todo_task': todo_task})

def delete_task_view(request, pk):
    todo_task = get_object_or_404(Todo, pk=pk)
    todo_task.delete()
    return render(request, 'task_delete.html', context={'todo_task': todo_task})

def edit_task_view(request, pk):
    todo_task = get_object_or_404(Todo, pk=pk)
    if request.method == "GET":
        context = {
            'status_list': STATUS_OF_TASK,
            'todo_task': todo_task
        }
        return render(request, 'task_edit.html', context=context)
    else:
        todo_task.description = request.POST.get('description')
        todo_task.status = request.POST.get('status')
        todo_task.lead_at = request.POST.get('lead_at')
        todo_task.detail_description = request.POST.get('detail_description')
        todo_task.save()
        return redirect('task_detail', pk=pk)





