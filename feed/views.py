from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView, UpdateView, DeleteView, ListView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.decorators import method_decorator
from django.contrib import messages
from django.db.models import Q
from . import models, form
# Create your views here.


@method_decorator(login_required, name="dispatch")
class home(LoginRequiredMixin, ListView):
    model = models.Post
    template_name ='feed/all_post.html'
    context_object_name = "posts"
    ordering = ["-created_at"] 

@method_decorator(login_required, name="dispatch")
class Profile(LoginRequiredMixin, ListView):
    model = models.Post
    template_name = "feed/profile.html"
    context_object_name = "posts"

    def get_queryset(self):
        return models.Post.objects.filter(user=self.request.user).order_by("-created_at")

@method_decorator(login_required, name="dispatch")  
class CreatePost(LoginRequiredMixin, CreateView):
    form_class = form.postform
    template_name = "feed/post_create&update.html"
    success_url = reverse_lazy("home")

    def form_valid(self, form):
        fruser = form.save(commit=False)
        fruser.user = self.request.user
        fruser.save()
        messages.success(self.request, 'Post Created Successfully')
        return super().form_valid(form)

@method_decorator(login_required, name="dispatch")    
class updatepost(LoginRequiredMixin, UpdateView):
    model = models.Post
    form_class = form.postform
    template_name = "feed/post_create&update.html"
    pk_url_kwarg = 'id'
    success_url = reverse_lazy("home")

    def form_valid(self, form):
        """If the form is valid, save the associated model."""
        messages.success(self.request, "Post Edit Successfully")
        return super().form_valid(form)
        
@method_decorator(login_required, name="dispatch")
class deletepost(LoginRequiredMixin, DeleteView):
    model = models.Post
    template_name = "feed/post_delete.html"
    pk_url_kwarg = 'id'
    success_url = reverse_lazy("home")

class PostListView(ListView):
    model = models.Post
    template_name = "feed/serch.html"  
    context_object_name = "posts"
    ordering = ["-created_at"]  

    def get_queryset(self):
        queryset = models.Post.objects.all()
        search_query = self.request.GET.get("q")
        filter_user = self.request.GET.get("user")
        filter_media = self.request.GET.get("media")
        filter_date = self.request.GET.get("date")

        if search_query:
            queryset = queryset.filter(Q(text__icontains=search_query)| Q(title__icontains= search_query) | Q(user__username__icontains= search_query) | Q(catagory__icontains= search_query))

        if filter_user:
            queryset = queryset.filter(user__username=filter_user)

        if filter_media == "text":
            queryset = queryset.filter(img='')
        elif filter_media == "image":
            queryset = queryset.filter(text ='')

        if filter_date == "oldest":
            queryset = queryset.order_by("created_at")
        else:
            queryset = queryset.order_by("-created_at")

        return queryset
    
class search(ListView):
    model = models.Post
    template_name = "components/nav.html"
    context_object_name = "posts"
    ordering = ["-created_at"]
    success_url = reverse_lazy("feed/serch.html")

    def get_queryset(self):
        queryset = models.Post.objects.all()
        search_query = self.request.GET.get("q")

        
        return queryset 

