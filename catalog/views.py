from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, TemplateView, CreateView, UpdateView
from django.views.generic.edit import FormView

from .forms import ContactForm, ProductForm
from .models import Product
from .utils import save_contact_to_file


class HomeView(TemplateView):
    """Обработка домашней страницы."""
    template_name = "catalog/home.html"


class ContactFormView(FormView):
    """Обработка формы обратной связи."""
    template_name = "catalog/contacts.html"
    form_class = ContactForm

    def form_valid(self, form):
        name = form.cleaned_data["name"]
        phone = form.cleaned_data["phone"]
        message = form.cleaned_data["message"]

        save_contact_to_file(name, phone, message)

        return HttpResponse(f"Спасибо, {name}! Ваше сообщение сохранено.")


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    template_name = "catalog/product_form.html"
    success_url = reverse_lazy('catalog:product_list')

class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    template_name = "catalog/product_form.html"
    success_url = reverse_lazy('catalog:product_list')


class ProductsListView(ListView):
    model = Product


class ProductDetailView(DetailView):
    model = Product
