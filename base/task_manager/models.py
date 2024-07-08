from django.db import models

class Task(models.Model):
    task_text = models.CharField(max_length=250)
    pub_date = models.DateTimeField(auto_now_add=True)
    done = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.task_text
    