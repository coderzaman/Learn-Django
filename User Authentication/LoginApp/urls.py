from django.urls import path
from LoginApp import views
from django.conf.urls.static import static
from django.conf import settings

app_name = 'login'

urlpatterns = [
    path('',views.index, name='index'),
    path('register/', views.register, name='register'),
    path('login/',views.user_login, name='user_login')
]

