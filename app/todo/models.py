from django.contrib.auth.models import User
from django.db import models


class Todo(models.Model):
    """Todo"""  # skip

    title = models.CharField(max_length=100)
    memo = models.TextField(
        blank=True,
        max_length=1000,
    )
    created = models.DateTimeField(auto_now_add=True)
    date_completed = models.DateTimeField(
        null=True,
        blank=True,
    )
    important = models.BooleanField(default=False)
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return f'{self.title=}'
