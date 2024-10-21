from django.shortcuts import render
from poetry.models import Poetry, Album
from poetry import forms
# Create your views here.
def index(request):
    poetry_list = Poetry.objects.order_by('first_name')
    
    diction = {
        "title": "The poets",
        "poetry_list": poetry_list
    }
    
    return render(request, 'poetry/index.html', context=diction)

# def form(request):
#     user_form = forms.user_form()
    
#     diction = {
#         "form_head": "Add Poets Information.....", 
#         "user_form": user_form
#     }
    
    # # check if the form is submitted
    # if request.method == "POST":
    #     # store submitted form
    #     user_form = forms.user_form(request.POST)
    #     diction.update({"user_form": user_form})
        
    #     # check if the form is valid
        
    #     if user_form.is_valid():
    #         # cleaned_data method helps to collect information from input fields
    #         # first_name = user_form.cleaned_data['first_name']
    #         # last_name = user_form.cleaned_data['last_name']
    #         # address = user_form.cleaned_data['address']
    #         # instrument = user_form.cleaned_data['instrument']
    #         field = user_form.cleaned_data['first_name']
    #         age = user_form.cleaned_data['age']
    #         even = user_form.cleaned_data['even_number']
    #         user_email = user_form.cleaned_data['user_email']
    #         # now store to dictionary
    #         diction.update({
    #             # "first_name": first_name,
    #             # "last_name": last_name,
    #             # "address": address,
    #             # "instrument": instrument,
    #             "field" : field,
    #             "age": age,
    #             "even_number": even,
    #             "user_email": user_email,
    #             "from_submitted": True
    #         })
    
    # return render(request, 'poetry/form.html', context=diction)


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