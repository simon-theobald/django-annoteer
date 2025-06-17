from django.db import models
from django.contrib.auth.models import User
from projects.models import Project


class Dataitem(models.Model):
    name = models.TextField()
    description = models.TextField(blank=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
