from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from catalog.apps import CatalogConfig
from .views import ProductsListView, ProductDetailView, ContactFormView, HomeView

app_name = CatalogConfig.name

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("contacts/", ContactFormView.as_view(), name="contacts"),
    path("products/", ProductsListView.as_view(), name="product_list"),
    path("products/<int:pk>/", ProductDetailView.as_view(), name="product_detail"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
