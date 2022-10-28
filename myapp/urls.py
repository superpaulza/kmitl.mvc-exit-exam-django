from django.contrib import admin
from django.urls import path, re_path
from . import views

# control page routes
urlpatterns = [
    path('', views.index, name='index'),
    path('upload/', views.upload, name='upload'),
    path('meme/', views.view_meme, name='meme'),
]
