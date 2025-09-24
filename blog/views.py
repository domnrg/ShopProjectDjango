from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, DeleteView
from .models import Post

class PostCreateView(CreateView):
    model = Post
    fields = ['title', 'content']
    template_name = "blog/post_form.html"
    success_url = reverse_lazy('blog:post_list')

class PostListView(ListView):
    model = Post
    template_name = "blog/post_list.html"

class PostDetailView(DetailView):
    model = Post
    template_name = "blog/post_detail.html"

class PostDeleteView(DeleteView):
    model = Post
    template_name = "blog/post_confirm_delete.html"
    success_url = reverse_lazy('blog:post_list')
