from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('LoginApp.urls')),
    path('admin/', admin.site.urls),
] 