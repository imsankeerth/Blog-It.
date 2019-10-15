from django.shortcuts import render
from django.views.generic import TemplateView,ListView,DetailView
from .models import Blog
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy
# Create your views here.

class HomePageView(ListView):
	model=Blog
	template_name = 'home.html'

class BlogDetailView(DetailView):
    model = Blog
    template_name = 'detail.html'
    context_object_name = 'batman'

class BlogCreateView(CreateView):
	model = Blog
	template_name = 'new_blog.html'
	fields = '__all__'

class BlogUpdateView(UpdateView):
	model = Blog
	template_name = 'blog_edit.html'
	fields = ['Name', 'text']

class BlogDeleteView(DeleteView):
    model = Blog
    template_name = 'blog_delete.html'
    context_object_name = 'batman'
    success_url = reverse_lazy('home')
