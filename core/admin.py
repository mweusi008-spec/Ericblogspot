from django.contrib import admin
from .models import News, ContactInfo


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ("title", "category", "created_at")
    list_filter = ("category", "created_at")
    search_fields = ("title", "content")


@admin.register(ContactInfo)
class ContactInfoAdmin(admin.ModelAdmin):
    list_display = ("email", "whatsapp", "telegram", "is_active")
    list_editable = ("is_active",)
