# from django import forms

# class user_form(forms.Form):
#     # Compare with html code
#     #  <label for="user_name">Full Name</label>
#     #  <input type="text" name="user_name", value="" required>
#     user_name = forms.CharField(label="Full Name",widget= forms.TextInput(
#     attrs={
#         'class':'form-control', 
#         'placeholder':'Enter Your Full Name'
#     }))
#     # here html text attribute name value is user_name what are same in here atrribute name
#     # We set html input field take input as text here CharField define take text
    
#     user_dob = forms.DateField(label="Date Of Birth", widget=forms.TextInput(
#         attrs={
#             'type':'date',
#             'class':'form-control',        
#         }
#     ))
#     # Compare with html code
#     #  <label for="user_name">User Email</label>
#     #  <input type="eamil" name="user_email", value="" required>
#     user_email = forms.EmailField(label="User Email", widget=forms.T)
#     # also same for this
    
#     # Here forms.CharField() and forms.EmailField() are some built-in function 
    
# from django import forms

# class user_form(forms.Form):
    # first_name = forms.CharField(label="First Name", widget=forms.TextInput(attrs={
    #     'class':'form-control mt-1 mb-3', 
    #     'placeholder':'Enter First Name',
    # }))
    # last_name = forms.CharField(label="Last Name", widget=forms.TextInput(attrs={
    #     'class':'form-control mt-1 mb-3', 
    #     'placeholder':'Enter Last Name',
    # }))
    
    # address = forms.CharField(widget=forms.TextInput(attrs={
    #     'class':'form-control mt-1 mb-3', 
    #     'placeholder':'Enter Address',
    # }))
    # instrument = forms.CharField(widget=forms.TextInput(attrs={
    #     'class':'form-control mt-1 mb-3', 
    #     'placeholder':'Enter Instrument',
    # }))
    
    
    # Boolean Field retrun true or false
    # By default it's required = True
    # unselected = False, selected = True
    # field = forms.BooleanField(required=False)
    
    # Date Field
    # field = forms.DateField(widget=forms.TextInput(attrs={
    #     'type':'date',
    #     'class':'form-control mt-1 mb-3',
    # }))
    
    # CharField more
    # does not allow to out range
    # does not allow to less than 6
    # does not allow to more than 15
    # field = forms.CharField(max_length=15, min_length=6, widget=forms.TextInput(attrs={
    #     'class':'form-control mt-1 mb-3',
    # }))


    # ChoiceField # select option
    # CHOICE_VALUES = (
    #     ('', 'Select Your Options'),
    #     ('1', 'Male'),
    #     ('2', 'Female'),
    #     ('0', 'Other'),
    # )
    
    # field = forms.ChoiceField(choices=CHOICE_VALUES, widget=forms.Select(attrs={
    #     'class':'form-control mt-1 mb-3',
    # }))
    
    # Radio Button with widget.RadioSelect
    # CHOICE_VALUES = (
    #     ('1', 'Male'),
    #     ('2', 'Female'),
    #     ('0', 'Other'),
    # )
    
    # field = forms.ChoiceField(choices=CHOICE_VALUES, widget=forms.RadioSelect)
    
    # Multiple select option. It's return a list
    # CHOICE_VALUES = (
    #     ('1', 'Male'),
    #     ('2', 'Female'),
    #     ('0', 'Other'),
    # )
    
    # field = forms.MultipleChoiceField(choices=CHOICE_VALUES)
    
    # multipe check box 
    # CHOICE_VALUES = (
    #     ('1', 'Male'),
    #     ('2', 'Female'),
    #     ('0', 'Other'),
    # )
    
    # field = forms.MultipleChoiceField(choices=CHOICE_VALUES, widget=forms.CheckboxSelectMultiple)
    
# From validataion 
# from django import forms
# # For validation beahaviour import 
# from django.core import validators
# from poetry import models



# class user_form(forms.Form):
    

        
#     def even_number_validator(value):
#         if value % 2 != 0:
#             raise forms.ValidationError("Please Insert Even Number")
    
#     first_name = forms.CharField(validators=[validators.MaxLengthValidator(16), validators.MinLengthValidator(6)],widget=forms.TextInput(attrs={
#         'class': 'form-control mb-4 mt-2'
#     }))
    
    # age = forms.IntegerField(validators=[validators.MaxValueValidator(200), validators.MinValueValidator(1)], widget=forms.TextInput(attrs={
    #     'class':'form-control  mb-4 mt-2'
    # }))
    
#     # We can Create our custom validator also. If we want even Number checker input validator do it like that
#     even_number = forms.IntegerField(validators=[even_number_validator],label="Even Number", widget=forms.NumberInput(attrs={
#         'placeholder': "Enter an even number",
#         'class': 'form-control mb-4 mt-2'
#     }))
    
#     user_email = forms.EmailField(widget=forms.EmailInput(attrs={
#         'placeholder': "Enter Your Email",
#         'class': 'form-control mb-4 mt-2'
#     }))
    
#     confirm_email = forms.EmailField(widget=forms.EmailInput(attrs={
#         'placeholder': "Confirm Your Email",
#         'class': 'form-control mb-4 mt-2'
#     }))
    
#     message = forms.CharField(widget=forms.Textarea)
    
#     def clean(self):
#         all_cleande_data = super().clean()
#         user_email = all_cleande_data['user_email']
#         confirm_email = all_cleande_data['confirm_email']

#         if user_email != confirm_email:
#             raise forms.ValidationError("Email Not Match")


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