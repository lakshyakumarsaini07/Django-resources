from django.shortcuts import render
from .models import Receipe
# Create your views here.


def receipe_list(request):
    receipe = Receipe.objects.all()
    return render(request, 'receipe/receipe_list.html', {'receipe': receipe})