from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from blog.views import PostListView, PostDetailView, PostCreateView, PostDeleteView, PostUpdateView

app_name = "blog"

urlpatterns = [
    path("", PostListView.as_view(), name="post_list"),
    path("post/<int:pk>/", PostDetailView.as_view(), name="post_detail"),
    path("post/create/", PostCreateView.as_view(), name="post_create"),
    path("post/<int:pk>/update", PostUpdateView.as_view(), name="post_update"),
    path("post/<int:pk>/delete", PostDeleteView.as_view(), name="post_delete"),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)