from django import forms
from poet import models

class PoetsForm(forms.ModelForm):
    class Meta:
        model = models.Poets
        fields = "__all__"
        
        labels = {
            'first_name':'First Name',
            'last_name':'Last Name',
        }
        
        widgets = {
            'first_name': forms.TextInput(attrs={
                'class': 'form-control mb-4 mt-2', 
                'placeholder': 'Enter first name',
                'label': "First Name"
            }),
            'last_name': forms.TextInput(attrs={
                'class': 'form-control mb-4 mt-2', 
                'placeholder': 'Enter last name'
            }),
            'address': forms.TextInput(attrs={
                'class': 'form-control mb-4 mt-2', 
                'placeholder': 'Enter Address'
            }),
            'instrument': forms.TextInput(attrs={
                'class': 'form-control mb-4 mt-2', 
                'placeholder': 'Enter Instrument'
            })
        }
        
class AlbumForm(forms.ModelForm):
    class Meta:
        model = models.Album
        fields = "__all__"
        
        labels = {
            'artist': "Poet Name",
            'name': "Album Name",
            'release_date': "Release Date", 
        }
        
        widgets = {
             'artist': forms.Select(attrs={
                'class': 'form-control mb-4 mt-2',
            }),
            'name': forms.TextInput(attrs={
                'class': 'form-control mb-4 mt-2', 
                'placeholder': 'Enter Album name'
            }),
            'release_date':forms.TextInput(attrs={
                'type':'date',
                'class': 'form-control mb-4 mt-2', 
            }),
            'rating': forms.Select(attrs={
                'class': 'form-control mb-4 mt-2', 
            })
        }
        