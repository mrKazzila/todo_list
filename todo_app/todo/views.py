from django.shortcuts import redirect, render
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from todo.forms import TodoCreateForm
from todo.models import Todo


class IndexView(TemplateView):
    template_name = 'todo/index.html'


class TodoListView(ListView):
    template_name = 'todo/current.html'
    queryset = Todo.objects.all()
    ordering = ('-important',)

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(
            user=self.request.user,
            date_completed__isnull=True,
        )


def create_todo_view(request):
    if request.method == 'GET':
        return render(request, 'todo/createtodo.html', {'form': TodoCreateForm()})
    else:
        form = TodoCreateForm(request.POST)
        new_todo = form.save(commit=False)
        new_todo.user = request.user
        new_todo.save()
        return redirect('todos:current')
