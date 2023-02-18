from django.urls import path

from todo.views import (TodoView)

app_name = 'todos'

urlpatterns = [
    path('', TodoView.as_view(), name='todo'),

]
