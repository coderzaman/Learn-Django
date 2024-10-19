from django.contrib import admin
from django.urls import path, include
# from first_app import views


# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('customer/', include('first_app.urls')),
# ]


# First_Project/urls.py


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('first_app.urls')),  # Include the app's urls
]

# Here path parameter indicate we need to write first_app/ after our URL 127.0.0.1:8000
# then write to view name
