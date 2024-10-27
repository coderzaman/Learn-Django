from django.urls import path
from LoginApp import views


app_name = 'poet'

urlpatterns = [
    path('',views.IndexView.as_view(), name='index'),
    path('poet_detail/<pk>/', views.PoetsDetail.as_view(), name='poet_detail')
]
