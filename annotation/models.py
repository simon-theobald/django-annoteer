from django.db import models
from django.contrib.auth.models import User
from django import forms

# Create your models here.
class Annotation(models.Model):
    STATUS_CHOICES = [
        (1, "Unannotated"),
        (2, "Annotated"),
        (3, "Finished Annotation")
    ]
    text = models.TextField(blank=True)
    status = models.PositiveIntegerField(choices=STATUS_CHOICES, default=1)
    finished_annotation = forms.ChoiceField(choices=("Ja", "Nein"))
    annotated_by = models.ForeignKey(User, on_delete=models.CASCADE)
    save_finished_annotation = models.BooleanField(default=False)
    last_modified_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='last_modified_by')
    last_annotated_at = models.DateTimeField(auto_now_add=True)
