# from django.urls import path
# from first_app import views


# urlpatterns = [
#     path('', views.index, name='index'),
#     path('contact/', views.contact, name='contact'),
# ]

from django.urls import path
from first_app import views

app_name = 'first_app'

urlpatterns = [
    path('', views.index, name='index'),  # The index view for the home page
    path('about/', views.about, name='about'),
]