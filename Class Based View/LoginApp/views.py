from django.shortcuts import render, redirect
from django.views.generic import View, TemplateView, ListView, DetailView
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