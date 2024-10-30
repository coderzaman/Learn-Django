from django.urls import path
from LoginApp import views


app_name = 'poet'

urlpatterns = [
    path('',views.IndexView.as_view(), name='index'),
    path('poet_detail/<pk>/', views.PoetsDetail.as_view(), name='poet_detail'),
    path('add_poet', views.AddPoet.as_view(), name='add_poet'),
    path('update_poet/<pk>/', views.UpdatePoet.as_view(), name='update_poet'),
    path('delete_poet/<pk>/', views.DeletePoet.as_view(), name='delete_poet')
]
