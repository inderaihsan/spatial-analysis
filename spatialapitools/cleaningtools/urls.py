from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
    path('init', views.init, name = 'init' ),
    path('luassegitiga', views.luas_segitiga, name = 'init' ),
    path('reading', views.read_data, name = 'readdata' ),
    path('radius', views.radius_filter, name = 'readdata' ),
]


