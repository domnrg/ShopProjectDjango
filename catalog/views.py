from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContactForm

def home(request):
    return render(request, 'home.html')

def contacts(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
        # Получение данных из формы
            name = form.cleaned_data['name']
            phone = form.cleaned_data['phone']
            message = form.cleaned_data['message']

            print(f"Новое сообщение: {name}, {phone}, {message}")

            # Сообщение об успешной отправке
            messages.success(request, f"Спасибо, {name}! Ваше сообщение получено.")
            return redirect('catalog:contacts')
    else:
        form = ContactForm()

    return render(request, 'contacts.html', {"form": form})
