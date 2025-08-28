from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(
        label="Имя",
        max_length=100,
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Ваше имя",
            "id": "name"
        })
    )
    phone = forms.CharField(
        label="Телефон",
        max_length=20,
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Контактный телефон",
            "id": "phone"
        })
    )
    message = forms.CharField(
        label="Сообщение",
        widget=forms.Textarea(attrs={
            "class": "form-control",
            "placeholder": "Ваше сообщение",
            "id": "message"
        })
    )
