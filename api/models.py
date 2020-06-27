from datetime import datetime

from django.db import models

# Create your models here.

class Task(models.Model):
  title = models.CharField(max_length=500)
  completed = models.BooleanField(default=False, blank=True, null=True)
  created_at = models.DateTimeField(default=datetime.now)

  def __str__(self):
    return self.title







