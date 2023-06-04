from django.contrib import admin
from django.urls import include, path

from todo.views import IndexView

urlpatterns = [
    path('enter2admin/', admin.site.urls, 'admin'),
    path('', IndexView.as_view(), name='index'),

    # Auth
    path('users/', include('users.urls', namespace='users')),

    # Todos
    path('todos/', include('todo.urls', namespace='todos')),
]
