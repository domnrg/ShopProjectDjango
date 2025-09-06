import csv
import os
from django.conf import settings


def save_contact_to_file(name: str, phone: str, message: str) -> None:
    """Сохраняет данные обратной связи в CSV-файл."""
    os.makedirs(settings.CONTACTS_DIR, exist_ok=True)

    with open(settings.CONTACTS_FILE, "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f, delimiter=";")
        writer.writerow([name, phone, message])
