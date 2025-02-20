from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home.as_view(), name='home'),
    path("Profile/", views.Profile.as_view(), name='profil'),
    path('postcreate/', views.CreatePost.as_view(), name='postcreate'),
    path('updatepost/<int:id>/', views.updatepost.as_view(), name='updatepost'),
    path('deletepost/<int:id>/', views.deletepost.as_view(), name='deletepost'),
]
