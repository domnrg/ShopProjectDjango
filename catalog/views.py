from django.http import HttpResponse
from django.shortcuts import render
from .forms import ContactForm
from .models import Product
from .utils import save_contact_to_file


def home(request):
    """Обработка домашней страницы."""
    return render(request, "home.html")


def contacts(request):
    """Обработка формы обратной связи."""
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            # Получение данных из формы
            name = form.cleaned_data["name"]
            phone = form.cleaned_data["phone"]
            message = form.cleaned_data["message"]

        # Вызов функции сохранения
        save_contact_to_file(name, phone, message)

        return HttpResponse(f"Спасибо, {name}! Ваше сообщение сохранено.")
    else:
        form = ContactForm()

    return render(request, "contacts.html", {"form": form})


def product_detail(request, pk):
    """Обработка страницы с подробной информацией о товаре"""
    product = Product.object.get(pk=pk)
    context = {"product": product}
    return render(request, "product_detail.html", context)

