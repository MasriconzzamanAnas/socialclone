from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import  LoginRequiredMixin
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, UpdateView, RedirectView
from django.contrib import messages
from django.contrib.auth import login as auth_login, logout as auth_logout
from . import models, form 

# Create your views here.

class singup(CreateView):
    form_class = form.signupfrom
    template_name = 'sign_log_chang.html'
    success_url = reverse_lazy("login")

    def form_valid(self, form):
        user= form.save()
        auth_login(self.request, user)
        redirect('home')
        messages.success(self.request, 'Accoutn Create Successfully')
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cerat'] = True
        return context

@method_decorator(login_required, name='dispatch')
class logout(RedirectView):
    url = reverse_lazy('login')

    def get(self, request, *args, **kwargs):
        auth_logout(request)
        messages.success(request, 'Logged Out Successfully')
        return super().get(request, *args, **kwargs)
    

