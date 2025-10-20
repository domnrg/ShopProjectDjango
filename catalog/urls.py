from django.urls import path
from django.views.decorators.cache import cache_page

from catalog.apps import CatalogConfig
from .views import ProductsListView, ProductDetailView, ContactFormView, HomeView, ProductCreateView, ProductUpdateView, \
    ProductDeleteView, ProductUnpublishView, ProductsByCategoryView

app_name = CatalogConfig.name

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("contacts/", ContactFormView.as_view(), name="contacts"),
    path("products/", ProductsListView.as_view(), name="product_list"),
    path("products/<int:pk>/", cache_page(60)(ProductDetailView.as_view()), name="product_detail"),
    path("product/create/", ProductCreateView.as_view(), name="product_create"),
    path("product/update/<int:pk>/", ProductUpdateView.as_view(), name="product_update"),
    path("product/<int:pk>/delete/", ProductDeleteView.as_view(), name="product_delete"),
    path('product/unpublish/<int:pk>/', ProductUnpublishView.as_view(), name='product_unpublish'),
    path('category/<int:category_id>/', ProductsByCategoryView.as_view(), name='products_by_category'),
]

