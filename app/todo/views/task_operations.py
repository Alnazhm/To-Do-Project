from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render, redirect, get_object_or_404
from todo.models import Todo, StatusChoices
from todo.forms import TaskForm


def add_view(request, *args, **kwargs):
    form = TaskForm()
    if request.method == 'GET':
        context = {'form': form}
        return render(request, 'create_task.html', context)
    form = TaskForm(request.POST)
    if not form.is_valid():
        context = {
            'form': form
        }
        return render(request, 'create_task.html', context)
    task = Todo.objects.create(**form.cleaned_data)
    return redirect('task_detail', pk=task.pk)


def detail_view(request, pk):
    todo_task = get_object_or_404(Todo, pk=pk)
    return render(request, 'task.html', context={'todo_task': todo_task})



def edit_task_view(request, pk):
    todo_task = get_object_or_404(Todo, pk=pk)
    if request.method == "GET":
        form = TaskForm(initial={
            'description': todo_task.description,
            'detail_description': todo_task.detail_description,
            'lead_at': todo_task.lead_at,
            'status': todo_task.status
        })
        return render(request, 'task_edit.html', context={'form': form, 'todo_task': todo_task})
    elif request.method == 'POST':
        form = TaskForm(data=request.POST)
        if form.is_valid():
            todo_task.description = form.cleaned_data['description']
            todo_task.detail_description = form.cleaned_data['detail_description']
            todo_task.status = form.cleaned_data['status']
            todo_task.lead_at = form.cleaned_data['lead_at']
            todo_task.save()
            return redirect(reverse('task_detail', kwargs={'pk': todo_task.pk}))
        else:
            return render(request, 'task_edit.html', context={'form': form, 'todo_task': todo_task})
def delete_task_view(request, pk):
    todo_task = get_object_or_404(Todo, pk=pk)
    return render(request, 'delete_confirm_page.html', context={'todo_task': todo_task})

def confirm_delete_task_view(request, pk):
    print("Hello")
    todo_task = get_object_or_404(Todo, pk=pk)
    todo_task.delete()
    return redirect('index')




