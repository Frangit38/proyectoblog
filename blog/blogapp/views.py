from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
from .forms import PostForm
from django.urls import reverse_lazy



class Homeview(ListView):
    model = Post
    template_name='home.html'
    ordering= ['-id']
class ArticleDetailView(DetailView):
    model=Post
    template_name= 'detailed_article.html'
class AddPostView(CreateView):
    model=Post
    form_class = PostForm
    template_name= 'newpost.html'
class UpdatePostView(UpdateView):
    model=Post
    template_name='edit.html'
    fields =['title', 'body']
class DeletePostView(DeleteView):
    model=Post
    template_name='deletepost.html'
    success_url= reverse_lazy('home')
class AboutSectionView(ListView):
    model = Post
    template_name='about.html'
