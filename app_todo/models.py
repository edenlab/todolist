from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Task(models.Model):
  description = models.CharField(max_length=100)
  due_date = models.DateTimeField(verbose_name="Due date")
  date_crea = models.DateTimeField(auto_now_add=True, auto_now=False,
                              verbose_name="Date of creation")
  is_done = models.BooleanField(default=False)

  def __str__(self):
    return self.description

  class Meta:
    ordering = ['due_date', 'description']




  # @property
  # def overdue(self):
  #   return self.due_date and self.due_date < datetime.utcnow()
