import csv
import os

from django.http import HttpResponse
from django.shortcuts import render
from .forms import ContactForm

def home(request):
    """Обработка домашней страницы."""
    return render(request, 'home.html')

def contacts(request):
    """Обработка формы обратной связи."""
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
        # Получение данных из формы
            name = form.cleaned_data['name']
            phone = form.cleaned_data['phone']
            message = form.cleaned_data['message']

        # Определяем путь к файлу
        file_path = os.path.join("data", "contacts.csv")

        # Создаём папку data, если её нет
        os.makedirs(os.path.dirname(file_path), exist_ok=True)

        # Записываем данные в CSV
        with open(file_path, "a", newline="", encoding="utf-8") as f:
            writer = csv.writer(f, delimiter=";")
            writer.writerow([name, phone, message])

        return HttpResponse(f"Спасибо, {name}! Ваше сообщение сохранено.")
    else:
        form = ContactForm()

    return render(request, 'contacts.html', {"form": form})
