from django.shortcuts import render
from LoginApp.forms import UserForm, UserInfoForm

# Create your views here.
def index(request):
    diction = {'title': 'Home Page'}
    return render(request, 'LoginApp/index.html', context=diction)

def register(request):
    register = False
    if request.method == 'POST':
        user_form = UserForm(data = request.POST)
        user_info_form = UserInfoForm(data=request.POST)

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
    return render(request, 'LoginApp/login.html', context=diction)