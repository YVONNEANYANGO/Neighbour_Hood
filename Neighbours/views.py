from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from . models import Neighbourhood,User,Business
from . forms import ProfileForm
from django.shortcuts import get_object_or_404

# Create your views here.

@login_required(login_url='accounts/login/')
def welcome(request):
    neighbourhood = Neighbourhood.objects.all()
    print(Neighbourhood)

    return render(request, 'welcome.html', {"neighbourhood":neighbourhood})


@login_required(login_url='accounts/login/')
def profile(request):
    # ivone = request.user.id
    profile = Profile.objects.all()
    # user = request.user

    return render(request, 'profile.html', {'profile':profile})

