from django.db import models

# Create your models here.
class Todo(models.Model):
    date_time = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=70)
    employee_id = models.CharField(max_length=50)
    shift_choice = (
        ('General', 'General'),
        ('Night', 'Night'),
        ('Morning', 'Morning'),
        ('Evening', 'Evening'),
    )
    shift = models.CharField(max_length=50,choices=shift_choice)
    arrival_choice = (
        ('Late', 'Late'),
        ('On time', 'On time')
    )
    arrival = models.CharField(max_length=70, choices=arrival_choice)
    remark = models.TextField(null=True, blank=True)