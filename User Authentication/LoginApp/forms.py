from django import forms
from  django.contrib.auth.models import User
from LoginApp.models import UserInfo


class UserForm(forms.ModelForm):
    class Meta():
        model = User
        fields = ('username', 'password', 'email')

        labels = {
            'email' : 'Email Address',
        }
       
        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'form-control mb-4 mt-2', 
                'placeholder': 'Enter Your Username'
            }),
            'password': forms.PasswordInput(attrs={
                'class': 'form-control mb-4 mt-2', 
                'placeholder': 'Enter Your Password'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control mb-4 mt-2', 
                'placeholder': 'Enter Your Email',
                'required': True,

            }),
        }
        
        
class UserInfoForm(forms.ModelForm):
    class Meta():
        model = UserInfo
        fields = ('facebook_id', 'profile_pic')
         
        labels = {
            'facebook_id' : 'Facebook Id',
            'profile_pic': 'Profile Picture'
        }
        
        widgets = {
            'facebook_id': forms.URLInput(attrs={
                'class': 'form-control mb-4 mt-2', 
                'placeholder': 'Enter Your Facebook Id'
            }),
            
            'profile_pic': forms.ClearableFileInput(attrs={
                'class': 'form-control mb-4 mt-2', 
            })
        }