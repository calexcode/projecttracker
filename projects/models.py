from django.db import models
from django.conf import settings
from django.utils import timezone

# Create your models here.
USER_MODEL = settings.AUTH_USER_MODEL


class Projects(models.Model):
    name = models.CharField(max_length=50)
    creator = models.ForeignKey(USER_MODEL, on_delete=models.CASCADE)
    created_on = models.DateTimeField(default=timezone.now)
    deadline = models.DateTimeField(blank=True)
    description = models.TextField(max_length=500)
    project_resources = models.FileField(upload_to='specs', blank=True)

    def __str__(self):
        return self.name
