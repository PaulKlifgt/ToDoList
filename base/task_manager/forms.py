from django import forms
from .models import Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['task_text']
        labels = {'task_text': 'Текст задачи'}
