from django.shortcuts import redirect, render
from django.utils import timezone

from todo.forms import TodoCreateForm


def get_task_list(queryset, user, is_completed: bool):
    return queryset.filter(
        user=user,
        date_completed__isnull=is_completed,
    )


def create_todo(request, redirect_to, template, form):
    render_data = {'form': form}
    if request.method == 'GET':
        return render(request, template, render_data)
    else:
        try:
            return _save_todo(request, redirect_to)
        except ValueError as e:
            render_data.update({'error': f'Bad date: {e}'})
            return render(request, template, render_data)


def _save_todo(request, redirect_to):
    form = TodoCreateForm(request.POST)
    new_todo = form.save(commit=False)
    new_todo.user = request.user
    new_todo.save()
    return redirect(redirect_to)


def complete_todo(todo, request_method, redirect_to):
    if request_method == 'POST':
        todo.date_completed = timezone.now()
        todo.save()
        return redirect(redirect_to)


def delete_todo(todo, request_method, redirect_to):
    if request_method == 'POST':
        todo.delete()
        return redirect(redirect_to)


def get_todo(request, todo, redirect_to, template):
    render_data = {'todo': todo, 'form': TodoCreateForm(instance=todo)}

    if request.method == 'GET':
        return render(request=request, template_name=template, context=render_data)
    else:
        try:
            return _update_open_todo(request=request, todo=todo, redirect_to=redirect_to)
        except ValueError:
            render_data.update({'error': 'Bad info'})
            return render(request=request, template_name=template, context=render_data)


def _update_open_todo(request, todo, redirect_to):
    form = TodoCreateForm(request.POST, instance=todo)
    form.save()
    return redirect(redirect_to)
