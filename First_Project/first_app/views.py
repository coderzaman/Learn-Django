from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

# def index(request):
#     return HttpResponse("<h1>Bismillahir Rahmanir Rahim</h1>")

# Creating and Linking Multiple Pages in Django Using Views and URL Patterns#
# Home Page
# Here when we write in href contact or about it make it to: 127.0.0.1:8000/contact/ or 127.0.0.1:8000/about/

# def index(request):
#     return HttpResponse("<h1>Home Page</h1> <a href='about/'>About Page</a> <a href='contact/'>Contact Page</a>") 

# here in href first / it make it to: 127.0.0.1:8000(index)
# and in href first / it make it to: 127.0.0.1:8000(index)  then contact/ goes it to 127.0.0.1:8000/contact

# def about(request):    
#     return HttpResponse("<h1>About Page</h1> <a href='/'>Home Page</a> <a href='/contact/'>Contact Page</a>") 


# here in href / it make it to: 127.0.0.1:8000(index)
# and in href first / it make it to: 127.0.0.1:8000(index)  then about/ goes it to 127.0.0.1:8000/about

# def contact(request):
#     return HttpResponse("<h1>Contact Page</h1> <a href='/'>Home Page</a> <a href='/about/'>About Page</a>") 


# URL Mappings
# If we need to create 10 application and that's views.py
# Each application has views.py every views has 10 view. So 10*10 = 100 view 
# We need to create 100 path in urls.py
# It's like to create 100 path in views.py[Not good practice]
# That's why we need to URL mapping. It make easier to our work

# We can create urls.py in frist application 
def index(request):
     return HttpResponse("<h1>Home Page</h1>") 
def contact(request):
     return HttpResponse("<h1>Contact Page</h1>") 
