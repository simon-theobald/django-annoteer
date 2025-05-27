from django.contrib import admin
from annotation.models import Annotation
from annotation.models import Annotate

# Register your models here.
admin.site.register(Annotate)
admin.site.register(Annotation)