from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from .models import Post

class PostCreateView(CreateView):
    model = Post
    fields = ['title', 'content', 'image']
    template_name = "blog/post_form.html"
    success_url = reverse_lazy('blog:post_list')

class PostListView(ListView):
    model = Post
    template_name = "blog/post_list.html"

    def get_queryset(self):
        return Post.objects.filter(is_published=True)

class PostDetailView(DetailView):
    model = Post
    template_name = "blog/post_detail.html"

    def get_object(self, queryset=None):
        object = super().get_object(queryset)
        object.counter += 1
        object.save(update_fields=["counter"])
        return object

class PostUpdateView(UpdateView):
    model = Post
    fields = ['title', 'content', 'image']
    template_name = "blog/post_form.html"

    def get_success_url(self):
        return reverse('blog:post_detail', kwargs={'pk': self.object.pk})


class PostDeleteView(DeleteView):
    model = Post
    template_name = "blog/post_confirm_delete.html"
    success_url = reverse_lazy('blog:post_list')
