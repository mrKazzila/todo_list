from django.urls import path

from todo.views import TodoView, create_todo_view

app_name = 'todos'

urlpatterns = [
    path('', TodoView.as_view(), name='todo'),
    path('create', create_todo_view, name='create'),
]
