from django.contrib import admin
from django.conf.urls import url
from django.urls import path, include
from restfulapi import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', views.users),
    path('users/<int:pk>/', views.user),
    path('register/', views.register),
    path('sign_in/', views.sign_in),
    path('send/', views.send),
    path('receive/', views.receive),
    path('delete/', views.delete),
    path('playlists/', views.playlists),
    path('playlists/<int:pk>/', views.playlist)
]
