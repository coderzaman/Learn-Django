from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'musician/index.html')


def add_musician(request):
    return render(request, 'musician/add_musician.html')