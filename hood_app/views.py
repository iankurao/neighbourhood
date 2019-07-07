from django.shortcuts import render,redirect,get_object_or_404
from . models import *
from .forms import *
from django.views import generic


# Create your views here.
def home(request):
    neighbourhoods = Neighbourhood.objects.all()
    return render(request, 'index.html',{"neighbourhoods":neighbourhoods,})

def neighbourhood(request):
    neighbourhoods = Neighbourhood.objects.all()
    return render(request,'index.html',{"neighbourhoods":neighbourhoods})


def profile(request):
    current_user = request.user
    profile = Profile.objects.all()

    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST,instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES,instance=request.user.profile)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            # message.success(request, f'Your account has been updated')
            return render(request,'registration/profile.html')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)


    context = {
        'u_form':u_form,
        'p_form':p_form
    }

    return render(request, 'registration/profile.html',locals())

def addneighbourhood(request):
    neighbourform = NeighbourhoodForm()
    neighbourform.owner = request.user
    if request.method == "POST":
        neighbourform = NeighbourhoodForm(request.POST,request.FILES)
        if neighbourform.is_valid():
           neighbourform.save()
           return render (request,'index.html')
        else:
           neighbourform=NeighbourhoodForm(request.POST,request.FILES)

    return render(request,'neighbourhood_form.html',{"neighbourform":neighbourform})

def neighbourhood_details(request,neighbourhood_id):
    businesses=Business.objects.filter(neighborhood=neighbourhood_id)
    posts=Post.objects.filter(neighborhood=neighbourhood_id)
    neighbourhood=Neighbourhood.objects.get(pk=neighbourhood_id)
    return render(request,'details.html',{'neighbourhood':neighbourhood,'businesses':businesses,'posts':posts})
