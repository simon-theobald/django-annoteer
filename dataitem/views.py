from django.shortcuts import render, get_object_or_404
from .models import Dataitem
# from .forms import AnnotationForm

def dataitem_detail(request, pk):
    dataitem = get_object_or_404(Dataitem, pk=pk)
    form = None  # we'll build this later
    return render(request, 'dataitem/dataitem_detail.html', {
        'dataitem': dataitem,
        'form': form,
    })
def index(request):
    dataitems = Dataitem.objects.all()
    return render(request, 'dataitem/index.html', {
        'dataitems': dataitems,
    })
