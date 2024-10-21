from django.shortcuts import render
from musician.models import Musician, Album
# Create your views here.


def index(request):
    # Get all musicians ordered by their name (like SELECT * FROM Musician ORDER BY name)
    musician_list = Musician.objects.order_by('name')
    
    # Create a dictionary to pass data to the template
    context = {
        "title": "Musician List",
        "musician": musician_list,  # Pass the queried data to the template
    }
    
    # Render the index.html template and pass the context
    return render(request, 'musician/index.html', context=context)



def add_musician(request):
    return render(request, 'musician/add_musician.html')