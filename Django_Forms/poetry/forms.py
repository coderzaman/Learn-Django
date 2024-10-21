from django import forms
from poetry import models

class MusicianForm(forms.ModelForm):
    class Meta:
        model = models.Poetry
        fields = "__all__"
        
        labels = {
            'first_name': 'Poet First Name',
            'last_name': 'Poet Last Name',
            'Address': 'Address of the Poet'
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