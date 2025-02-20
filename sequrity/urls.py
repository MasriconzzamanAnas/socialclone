from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name= 'login.html'), name='login'),
    path('singup/', views.singup.as_view(), name='signup'),
    # path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('logout/', views.logout.as_view(), name='logout'),

]
