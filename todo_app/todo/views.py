from django.shortcuts import redirect, render
from django.views.generic.base import TemplateView

from todo.forms import TodoCreateForm


class IndexView(TemplateView):
    template_name = 'todo/index.html'


class TodoView(TemplateView):
    template_name = 'todo/index.html'


def create_todo_view(request):
    if request.method == 'GET':
        return render(request, 'todo/createtodo.html', {'form': TodoCreateForm()})
    else:
        form = TodoCreateForm(request.POST)
        new_todo = form.save(commit=False)
        new_todo.user = request.user
        new_todo.save()
        return redirect('todos:todo')
