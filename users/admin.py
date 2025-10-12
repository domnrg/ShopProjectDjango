from django.contrib import admin

from users.models import User

@admin.register(User)
class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        "username",
        "email",
        "phone_number",
        "country",
    )
    search_fields = (
        "username",
        "email",
    )

