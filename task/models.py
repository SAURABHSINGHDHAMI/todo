from django.db import models

class ToDoTask(models.Model):
    start_by = models.TimeField()
    end_by = models.TimeField()
    task = models.CharField(max_length = 100)
    note = models.CharField(max_length = 300)
    status = models.BooleanField(default = False)

    def __str__(self):
        return self.task
    
    class Meta:
        ordering = ['start_by']