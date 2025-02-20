from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home.as_view(), name='home'),
    path("Profile/", views.Profile.as_view(), name='profil')
]
