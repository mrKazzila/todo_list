from django.forms import ModelForm

from .models import Todo


class TodoCreateForm(ModelForm):
    """Create todo form"""  # skip

    class Meta:
        model = Todo
        fields = ('title', 'memo', 'important')
