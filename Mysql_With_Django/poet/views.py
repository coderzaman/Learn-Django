from django.shortcuts import render
from poet import forms
from poet import models
from django.shortcuts import redirect
from django.db.models import Avg

# Create your views here.
def index(request):
    poets = models.Poets.objects.order_by('first_name')
    diction = {'title': "Poets", 'poets':poets}
    return render(request, 'poet/index.html', context=diction)



def add_poet(request):    
    form = forms.PoetsForm()
   
    if request.method == 'POST':
        form = forms.PoetsForm(request.POST)
        
        if form.is_valid():
            form.save(commit=True)
            return redirect('poet:index')

    diction = {'title': "Add Poet", 'form': form}
    return render(request, 'poet/add_poet.html', context=diction)





def add_album(request):
    form = forms.AlbumForm()
    
    if request.method == "POST":    
        form = forms.AlbumForm(request.POST)
    
        if form.is_valid():
            form.save(commit=True)
            return redirect('poet:index')
        
    diction = {'title': "Add Album",'form':form}
    return render(request, 'poet/add_album.html', context=diction)





def album_list(request, poet_id):
    poet_info = models.Poets.objects.get(pk=poet_id)
    album_info = models.Album.objects.filter(artist=poet_id).order_by('release_date')
    poet_rating = models.Album.objects.filter(artist=poet_id).aggregate(Avg('rating'))
    diction = {'title': "Album List", 'poet_info': poet_info, 'album_info':album_info, 'poet_rating':poet_rating,}
    
    return render(request, 'poet/album_list.html', context=diction)




def edit_poet(request, poet_id):
    poet_info = models.Poets.objects.get(pk=poet_id)
    form = forms.PoetsForm(instance=poet_info)
    
    if request.method == 'POST':
        form = forms.PoetsForm(request.POST, instance=poet_info)
        if form.is_valid():
            form.save(commit=True)
            return redirect('poet:index')
    diction = {'form':form, 'poet_id':poet_id, 'title':"Modify Poet"}
    return render(request, 'poet/edit_poet.html', diction)





def edit_album(request, album_id):
    album_info = models.Album.objects.get(pk=album_id)
    form = forms.AlbumForm(instance=album_info)
    diction = {'form':form, 'album_id':album_id}
    
    if request.method == 'POST':
        form = forms.AlbumForm(request.POST, instance=album_info)
        if form.is_valid:
            form.save(commit=True)
            poet_id = models.Album.objects.get(id=album_id).artist.id
            return redirect('poet:album_list', poet_id)

    return render(request, 'poet/edit_album.html', context=diction)





def delete_poet(request, delete_id):
    diction = {}
    try:
        poet = models.Poets.objects.get(pk=delete_id)  
        poet.delete() 
        diction.update({'delete_message': "Deleted Successfully"})
        return render(request, 'poet/delete.html', diction)
    except models.Poets.DoesNotExist:
        diction.update({'delete_message': "Not found!"})
        return render(request, 'poet/delete.html', diction)



def delete_album(request, delete_id):
    diction = {}
    try:
        poet = models.Album.objects.get(pk=delete_id)  
        poet.delete() 
        diction.update({'delete_message': "Deleted Successfully"})
        return render(request, 'poet/delete.html', diction)
    except models.Album.DoesNotExist:
        diction.update({'delete_message': "Not found!"})
        return render(request, 'poet/delete.html', diction)

   