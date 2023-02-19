from django.forms import ModelForm

from todo.models import Todo


class TodoCreateForm(ModelForm):
    class Meta:
        model = Todo
        fields = ('title', 'memo', 'important')
