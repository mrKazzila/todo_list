from django.urls import path

from todo.views import TodoListView, create_todo_view

app_name = 'todos'

urlpatterns = [
    path('', TodoListView.as_view(), name='current'),
    path('create', create_todo_view, name='create'),
]
