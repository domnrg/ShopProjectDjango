from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from blog.views import PostListView, PostDetailView
from catalog.apps import CatalogConfig

app_name = CatalogConfig.name

urlpatterns = [
    path("", PostListView.as_view(), name="post_list"),
    path("<int:pk>/", PostDetailView.as_view(), name="post_detail"),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)