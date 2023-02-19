from django import forms
from django.forms import ModelForm

from todo.models import Todo


class TodoCreateForm(ModelForm):
    class Meta:
        model = Todo
        fields = ('title', 'memo', 'important', )

    title = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control py-4'},
        ),
    )
    memo = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control py-4'},
        ),
    )
    # important = forms.BooleanField(
    #     required=False,
    #     # widget=forms.ChoiceField(
    #     #
    #     #     attrs={'class': 'form-control py-4'},
    #     # ),
    # )

    def save(self, commit=False):
        new_form = super().save(commit=False)
        return new_form