from django.db import models

# For using Django building model(table) of db import a User model 
from django.contrib.auth.models import User

# You are use username, password, email from User model

# Create your models here.

# If we add any filed not in User model we need create another model

class UserInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    facebook_id = models.URLField(blank=True)
    profile_pic = models.ImageField(upload_to= 'profile_pics', blank=True)
    email = models.EmailField(unique=True, null=True)
    
    def __str__(self):
        return self.user.username