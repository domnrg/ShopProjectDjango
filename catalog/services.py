from django.core.cache import cache

from catalog.models import Product
from config.settings import CACHE_ENABLED


def get_products_by_category(category_id):
    """Возвращает список опубликованных продуктов по категории."""
    return Product.objects.filter(category_id=category_id, is_published=True)

def get_products_from_cache():
    if not CACHE_ENABLED:
        return Product.objects.filter(is_published=True).select_related('category')
    key = "products_list"
    products = cache.get(key)
    if products is not None:
        return products
    products = Product.objects.filter(is_published=True).select_related('category')
    cache.set(key, products)
    return products

