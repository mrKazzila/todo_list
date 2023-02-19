from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView

from todo.forms import TodoCreateForm
from todo.models import Todo


class IndexView(TemplateView):
    template_name = 'todo/index.html'


def create_todo_view(request):
    if request.method == 'GET':
        return render(request, 'todo/createtodo.html', {'form': TodoCreateForm()})
    else:
        try:
            form = TodoCreateForm(request.POST)
            new_todo = form.save(commit=False)
            new_todo.user = request.user
            new_todo.save()
            return redirect('todos:current')
        except ValueError as e:
            return render(
                request,
                'todo/createtodo.html',
                {
                    'form': TodoCreateForm(),
                    'error': f'Bad date: {e}',
                },
            )


class TodoListView(ListView):
    template_name = 'todo/todos.html'
    queryset = Todo.objects.all()
    ordering = ('-important',)

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(
            user=self.request.user,
            date_completed__isnull=True,
        )


def todo_view(request, todo_pk):
    todo = get_object_or_404(Todo, pk=todo_pk, user=request.user)
    if request.method == 'GET':
        form = TodoCreateForm(instance=todo)
        return render(request, 'todo/todo.html', {'todo': todo, 'form': form})
    else:
        try:
            form = TodoCreateForm(request.POST, instance=todo)
            form.save()
            return redirect('todos:current')
        except ValueError:
            form = TodoCreateForm(instance=todo)
            return render(request, 'todo/viewtodo.html', {'todo': todo, 'form': form, 'error': 'Bad info'})


def compete_todo_view(request, todo_pk):
    todo = get_object_or_404(Todo, pk=todo_pk, user=request.user)
    if request.method == 'POST':
        todo.date_completed = timezone.now()
        todo.save()
        return redirect('todos:current')


def delete_todo_view(request, todo_pk):
    todo = get_object_or_404(Todo, pk=todo_pk, user=request.user)
    if request.method == 'POST':
        todo.delete()
        return redirect('todos:current')


class CompletedTodoListView(ListView):
    template_name = 'todo/completed.html'
    queryset = Todo.objects.all()
    ordering = ('-date_completed', '-important')

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(
            user=self.request.user,
            date_completed__isnull=False,
        )
