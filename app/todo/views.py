from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView

from .forms import TodoCreateForm
from .models import Todo
from .todo_services import complete_todo, create_todo, delete_todo, get_task_list, get_todo


class IndexView(TemplateView):
    """Main page"""

    template_name = 'todo/index.html'


@login_required
def create_todo_view(request):
    """Create todos page"""
    template_name = 'todo/createtodo.html'
    form = TodoCreateForm()
    redirect_url = 'todos:current'

    return create_todo(
        request=request,
        template=template_name,
        redirect_to=redirect_url,
        form=form,
    )


class TodoListView(ListView):
    """Page with todos"""

    template_name = 'todo/todos.html'
    queryset = Todo.objects.all()
    ordering = ('-created', '-important')

    def get_queryset(self):
        return get_task_list(
            queryset=super().get_queryset(),
            user=self.request.user,
            is_completed=True,
        )


class CompletedTodoListView(ListView):
    """Page with completed todos"""

    template_name = 'todo/completed.html'
    queryset = Todo.objects.all()
    ordering = ('-date_completed', '-important')

    def get_queryset(self):
        return get_task_list(
            queryset=super().get_queryset(),
            user=self.request.user,
            is_completed=False,
        )


@login_required
def todo_view(request, todo_pk):
    """Todo page"""  # skip
    return get_todo(
        request=request,
        todo=get_object_or_404(Todo, pk=todo_pk, user=request.user),
        template='todo/todo.html',
        redirect_to='todos:current',
    )


@login_required
def compete_todo_view(request, todo_pk):
    """Mark todo as completed"""  # skip
    return complete_todo(
        todo=get_object_or_404(Todo, pk=todo_pk, user=request.user),
        request_method=request.method,
        redirect_to='todos:current',
    )


@login_required
def delete_todo_view(request, todo_pk):
    """Delete todo"""  # skip
    return delete_todo(
        todo=get_object_or_404(Todo, pk=todo_pk, user=request.user),
        request_method=request.method,
        redirect_to='todos:current',
    )
