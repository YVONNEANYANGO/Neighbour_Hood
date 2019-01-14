from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from . models import Neighbourhood,User,Business
from . forms import ProfileForm
from django.shortcuts import get_object_or_404
from . models import Profile
from . forms import NeighbourhoodForm

# Create your views here.

@login_required(login_url='accounts/login/')
def welcome(request):
    neighbourhoods = Neighbourhood.objects.all()

    return render(request, 'welcome.html', {"neighbourhoods":neighbourhoods})


@login_required(login_url='accounts/login/')
def profile(request):
    # ivone = request.user.id
    profile = Profile.objects.all()
    # user = request.user

    return render(request, 'profile.html', {'profile':profile})


def newprofile(request):
#  ivone = request.user.id
 profile = Profile.objects.all()
 if request.method == 'POST':
   instance = get_object_or_404(Profile)
   form = ProfileForm(request.POST, request.FILES,instance=instance)
   if form.is_valid():
     form.save()

   return redirect('welcome')

 else:
   form = ProfileForm()

 return render(request, 'newprofile.html',{'form':form,'profile':profile})
  

@login_required(login_url='/accounts/login/')
def neighbourhood(request):
    neighbourhoods = Neighbourhood.ojects.all().order_by()

    return render(request, "welcome.html", {"neighbourhoods":neighbourhoods})


@login_required(login_url='/accounts/login/')
def add_neighbourhood(request):
   if request.method =='POST':
       neighbourhoods = Neighbourhood.objects.filter(user=request.user)
       form = NeighbourhoodForm(request.POST)
       if form.is_valid():
           neighbourhood = form.save(commit = False)
           neighbourhood.user = request_user
           neighbourhood.save()
           return redirect('welcome')
   else:
       form = NewHoodForm()
       return render(request,'add_neighbourhood.html',{"form":form})

@login_required(login_url='/accounts/login/')
def business(request):
    business = Business.ojects.get_all()

    return render(request, "welcome.html", {"business":business})


def search_results(request):

    if 'neighbourhood' in request.GET and request.GET["neighbourhood"]:
        search_term = request.GET.get("neighbourhood")
        searched_neighbourhood = Project.search_by_neighbourhood_id(search_term)

        message = f"{search_term}"

        return render(request, 'search.html', {"message":message,"neighbourhood_id": searched_neighbourhood})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})

def search_results(request):

    if 'business' in request.GET and request.GET["business"]:
        search_term = request.GET.get("business")
        searched_business = Project.search_by_subject(search_term)

        message = f"{search_term}"

        return render(request, 'search.html', {"message":message,"flashes": searched_flashes})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})

