from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Dataitem(models.Model):

    name = models.CharField(max_length=3)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    uploaded_file = models.FileField(upload_to='uploads/', null=True, blank=True)


    def __str__(self):
        return self.name
