from django.db import models

class Task(models.Model):
    title =models.CharField(max_length=100)
    description = models.TextField(help_text = "The description of the Task.")