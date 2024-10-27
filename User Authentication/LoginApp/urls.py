from django.urls import path
from LoginApp import views
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.urls import static, staticfiles_urlpatterns

app_name = 'login'

urlpatterns = [
    path('',views.index, name='index'),
    path('register/', views.register, name='register'),
    path('login/',views.user_login, name='user_login'),
    path('logout/', views.user_logout, name='logout')
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
