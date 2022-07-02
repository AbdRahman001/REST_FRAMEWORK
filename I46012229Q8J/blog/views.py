from dataclasses import fields
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView 
from .models import Post

class PostCreateView(CreateView):
    model = Post
    fields = "__all__"
    success_url: reverse_lazy("blog:all")

class PostListView(ListView):
    model = Post
       
class PostDetailView(DetailView):
    model = Post
    
class PostUpdateView(UpdateView):
    model = Post
    fields = "__all__"
    success_url = reverse_lazy("blog:all")

class PostDeleteView(DeleteView):
    model = Post
    fields = "__all__"
    success_url = reverse_lazy("blog:all")    
# Create your views here.
