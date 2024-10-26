from django.urls import path
from poet import views 

app_name = 'poet'

urlpatterns = [
    path('', views.index, name="index"),
    path('add_poet/',views.add_poet, name="add_poet"),
    path('add_album/',views.add_album, name="add_album"),
    path('album_list/<int:poet_id>/', views.album_list, name="album_list"),
    path('edit_poet/<int:poet_id>/', views.edit_poet, name="edit_poet"),
    path('edit_album/<int:album_id>/', views.edit_album, name="edit_album"),
    path('delete_poet/<int:delete_id>/', views.delete_poet, name="delete_poet"),
    path('delete_album/<int:delete_id>/', views.delete_album, name="delete_album")
]
