# from django.urls import path
# from first_app import views


# urlpatterns = [
#     path('', views.index, name='index'),
#     path('contact/', views.contact, name='contact'),
# ]

from django.urls import path
from first_app import views

urlpatterns = [
    path('', views.index, name='index'),
    path('contact/', views.contact, name='contact'),
]
