from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.views.generic import TemplateView, CreateView, UpdateView, DeleteView, ListView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.decorators import method_decorator
from . import models, form
# Create your views here.

def home(request):
    return render(request, 'feed/all_post.html')

class home(ListView):
    model = models.Post
    template_name ='feed/all_post.html'
    context_object_name = "posts"
    ordering = ["-created_at"] 


class Profile( ListView):
    model = models.Post
    template_name = "feed/profile.html"
    context_object_name = "posts"

    def get_queryset(self):
        return models.Post.objects.filter(user=self.request.user).order_by("-created_at")
    

