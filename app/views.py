
from django.shortcuts import render
from .models import Avtomobil
from django.views import View

# Create your views here.


def main(request):
    contex = {
        'main' : Avtomobil.objects.all(),
        'all_avto': Avtomobil.objects.all(),
    }
    return render(request, 'blog/basic.html', contex)
    
def all_avto(request):
    contex = {
        'all_avto':Avtomobil.objects.all(),
    }
    return render(request, 'blog/avtolar.html', contex)