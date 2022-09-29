from django.shortcuts import render
from django.core.handlers.wsgi import WSGIRequest

from todo.models import Todo


def index_view(request: WSGIRequest):
    todo_tasks = Todo.objects.all()
    context = {
        'todo_tasks': todo_tasks
    }
    return render(request, 'index.html', context=context)