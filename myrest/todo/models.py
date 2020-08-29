from django.db import models


class ToDoItem(models.Model):
    text = models.CharField(max_length=250)
    done = models.BooleanField()

    def __str__(self):
        return f'Task { self.text } is { "not" if not self.done else "" } done'
