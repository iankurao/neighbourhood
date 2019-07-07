from django.shortcuts import render,redirect,get_object_or_404
from django.views import generic


# Create your views here.
def home(request):
    neighbourhoods = Neighbourhood.objects.all()
    return render(request, 'index.html',{"neighbourhoods":neighbourhoods,})
