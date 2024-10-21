from django.urls import path
from poetry import views

app_name = 'poetry'

urlpatterns = [
    path('', views.index, name='index'),
    path('form/', views.form, name='form')
]