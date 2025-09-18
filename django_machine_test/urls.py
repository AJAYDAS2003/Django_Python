from django.contrib import admin
from django.urls import path
from Nimap_django.views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),  # root URL -> home view
]
