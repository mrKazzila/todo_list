from django.contrib.auth.decorators import login_required
from django.urls import path

from todo.views import (CompletedTodoListView, TodoListView, compete_todo_view,
                        create_todo_view, delete_todo_view, todo_view)

app_name = 'todos'

urlpatterns = [
    path('', login_required(TodoListView.as_view()), name='current'),
    path('create', create_todo_view, name='create'),
    path('completed', login_required(CompletedTodoListView.as_view()), name='completed'),
    path('todo/<int:todo_pk>/', todo_view, name='viewtodo'),
    path('todo/<int:todo_pk>/complete', compete_todo_view, name='complete'),
    path('todo/<int:todo_pk>/delete', delete_todo_view, name='delete'),
]
