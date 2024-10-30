from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import View, TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.http import HttpResponse 
from LoginApp.models import Poets

# class IndexView(View):
#     def get(self, request):
#         return render(request, 'LoginApp/index.html', context=None)
    
    
# class IndexView(TemplateView):
#     template_name = 'LoginApp/index.html'
    
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['s_text1'] = "Sample Text 1"
#         context['s_text2'] = "Sample Text 2"
        
#         return context


# ListView is build in class which provide models information as list     
class IndexView(ListView):
    context_object_name = 'poet_list'
    model = Poets
    template_name = 'LoginApp/index.html'
    

# DetailView is build in class which provide one row of a models
class PoetsDetail(DetailView):
    context_object_name = 'poet'
    model = Poets
    template_name = 'LoginApp/poet_detail.html'
    


# Create View Provide readymade from 
class AddPoet(CreateView):
    fields = ('first_name','last_name', 'address', 'instrument')
    model = Poets
    template_name = 'LoginApp/poets_form.html'

    def get_form(self, form_class=None):
        # Get the form using the superclass method
        form = super().get_form(form_class)
        
        # Add a CSS class to each field
        for visible_field in form.visible_fields():
            visible_field.field.widget.attrs['class'] = 'form-control mt-2'
        
        return form


class UpdatePoet(UpdateView):
    fields =  ('first_name','last_name', 'address', 'instrument')
    model = Poets
    
    def get_form(self, form_class=None):
        # Get the form using the superclass method
        form = super().get_form(form_class)
        
        # Add a CSS class to each field
        for visible_field in form.visible_fields():
            visible_field.field.widget.attrs['class'] = 'form-control mt-2'
        
        return form


# DeleteView 
class DeletePoet(DeleteView):
    model = Poets
    success_url = reverse_lazy('poet:index')
    template_name = 'LoginApp/delete_poet.html'
    context_object_name = 'poets'