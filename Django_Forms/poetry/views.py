from django.shortcuts import render
from poetry.models import Poetry, Album
from poetry import forms
from datetime import datetime
# Create your views here.
def index(request):
    poetry_list = Poetry.objects.order_by('first_name')
    
    diction = {
        "title": "The poets",
        "number": "5",
        "poetry_list": poetry_list,
        "list":[1,2,3,4],
        "list2":[6,7,8,9],
        "text":"Demo Text",
        "date": datetime.now().date,
        "rel_date": Album.objects.get(pk=1)
    }
    
    return render(request, 'poetry/index.html', context=diction)


def form(request):
    musicican_form = forms.MusicianForm()
    
    if request.method == 'POST':
        new_form = forms.MusicianForm(request.POST)
        
        if new_form.is_valid():
            new_form.save(commit=True)
            return index(request)
    
        
    diction = {
        "form_head": "Add Poets Information.....", 
        "musicican_form": musicican_form
    }

    return render(request, 'poetry/form.html', context=diction)