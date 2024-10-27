from django.shortcuts import render, redirect
from LoginApp.forms import UserForm, UserInfoForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from LoginApp.models import UserInfo
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
# Create your views here.
def index(request):
    diction = {'title': 'Home Page'}
    
    if request.user.is_authenticated:
        current_user = request.user
        user_id = current_user.id
        user_basic_info = User.objects.get(pk=user_id)
        user_more_info = UserInfo.objects.get(user__pk=user_id)
        
        diction.update({
            'title': current_user.username,
            'user_basic_info':user_basic_info,
            'user_more_info':user_more_info,
        })
            
    return render(request, 'LoginApp/index.html', context=diction)

def register(request):
    register = False
    if request.method == 'POST':
        user_form = UserForm(data = request.POST)
        user_info_form = UserInfoForm(data=request.POST)
        # user_info_form = UserInfoForm(data=request.POST, files=request.FILES)  # Pass request.FILES here#

        if user_form.is_valid() and user_info_form.is_valid():
            user = user_form.save(commit=False)
            
            user.set_password(user_form.cleaned_data['password'])
            user.save()
            
            user_info = user_info_form.save(commit=False)
            
            if 'profile_pic' in request.FILES:
                user_info.profile_pic = request.FILES['profile_pic']
            
            user_info.user = user
            user_info.save()
            register = True
    else:
        user_form = UserForm()
        user_info_form = UserInfoForm()

    diction = {'title':'User Registration','user_form':user_form, 'user_info_form': user_info_form, 'register':register}
    
    return render(request, 'LoginApp/register.html', context=diction)


def user_login(request):
    diction = {'title':"Login"}
    
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
         
        try:
            user = User.objects.get(username=username)
            
            if not user.is_active:
                diction.update({
                    'error_message':"Your Profile is Not Active"
                })
                return render(request, 'LoginApp/login.html', context=diction)   
            
            user = authenticate(username=username, password=password)
            if user:
                login(request,user)
                return redirect('login:index')
            else:
                diction.update({
                    'error_message':"Username and Password Not Match"
                })    
        except User.DoesNotExist:
            diction.update({
                'error_message':"Username Not Found"
            })
    
    return render(request, 'LoginApp/login.html', context=diction)


@login_required
def user_logout(request):
    logout(request)
    return redirect('login:index')
