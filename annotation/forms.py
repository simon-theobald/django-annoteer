from django import forms
from .models import Annotation


class AnnotationForm(forms.ModelForm):
    class Meta:
        model = Annotation
        # Use real model fields
        fields = ["text", "status", "finished_annotations"]
