from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from .models import Profile
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import CustomUserCreationForm, ProfileForm
#from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def loginUser(request):
    page = 'login'
    if request.user.is_authenticated:
        return redirect('profiles')

    if request.method =='POST':
        #print(request.POST)
        username = request.POST['username']
        password = request.POST['password']

        try:
            user = User.objects.get(username=username)
        except:
            print('Username does not exist')
            messages.error(request, 'Username does not exist')

        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('profiles')
        else:
            print('Username OR password is incorrect')
            messages.error(request, 'Username OR password is incorrect')

    return render(request, 'profiles/login_register.html')

def logoutUser(request):
    logout(request)
    messages.error(request, 'User was logged out')
    return redirect('login')

def registerUser(request):
    page = 'register'
    #form = UserCreationForm()
    form = CustomUserCreationForm()
    if request.method == 'POST':
        #form = UserCreationForm(request.POST)
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()    
            messages.success(request, 'User successfully created')
            login(request, user)
            return redirect('edit-account')
        else:
            print('Error ocurred during registration')
            messages.success(request, 'An error has ocurred during registration')

    context = {
        'page' : page,
        'form' : form
    }
    return render(request, 'profiles/login_register.html', context)

def profiles(request):
    profiles = Profile.objects.all()
    context = {
        'profiles' : profiles
    }
    return render(request, 'profiles/profiles.html', context)



def userProfile(request, pk):
    profile = Profile.objects.get(id=pk)
    top_skills = profile.skill_set.exclude(description__exact="")
    other_skills = profile.skill_set.filter(description ="")

    context= {
        'profile': profile,
        'top_skills': top_skills,
        'other_skills' : other_skills,
    }
    template = r'profiles\user-profile.html'
    return render(request, template, context)

@login_required(login_url= 'login')
def userAccount(request):
    profile = request.user.profile

    skills = profile.skill_set.all()
    projects = profile.project_set.all()

    print(f'project {projects}')

    context = {
        'profile' : profile,
        'skills' : skills,
        'projects' : projects
    }
    return render (request, 'profiles/account.html' , context)

@login_required(login_url='login')
def editAccount(request):
    profile = request.user.profile
    form = ProfileForm(instance=profile)
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('account')
    context = {
        'form':form,
    }
    return render(request, 'profiles/profile_form.html', context)
