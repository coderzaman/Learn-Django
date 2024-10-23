from django.urls import path
from poet import views 

app_name = 'poet'

urlpatterns = [
    path('', views.index, name="index"),
    path('add_poet/',views.add_poet, name="add_poet"),
    path('add_album/',views.add_album, name="add_album"),
    path('album_list/<int:poet_id>/', views.album_list, name="album_list")
]
