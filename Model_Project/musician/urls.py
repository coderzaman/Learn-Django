from django.urls import path
from musician import views
app_name = 'musician'
urlpatterns = [
    path('', views.index, name='index'),
    path('add_musician/', views.add_musician, name='add_musician'),
]