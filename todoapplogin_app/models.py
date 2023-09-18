from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse

# Create your models here.

def one_week_hence():
    return timezone.now() + timezone.timedelta(days=7) # type: ignore
def now():
    return timezone.now()


class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=200, null=True, blank=True) # type: ignore
    description = models.TextField(null=True, blank=True)
    complete = models.BooleanField(default=False)
    create = models.DateTimeField(default=now, null=True, blank=True)
    due_date = models.DateTimeField(default=one_week_hence, null=True, blank=True)
    
    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ["complete"]