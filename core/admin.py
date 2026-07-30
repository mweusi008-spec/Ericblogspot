from django.contrib import admin
from django.contrib import messages
from django.shortcuts import redirect
from .models import News, ContactInfo


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ("title", "category", "is_emergency", "created_at")
    list_filter = ("category", "is_emergency", "created_at")
    search_fields = ("title", "content")
    list_editable = ("is_emergency",)
    list_display_links = ("title",)
    fieldsets = (
        (None, {
            "fields": ("title", "category", "content"),
        }),
        ("Emergency Settings", {
            "fields": ("is_emergency",),
            "description": "Check this box ONLY for urgent emergency alerts that should appear as a scrolling ribbon on all pages.",
        }),
    )


@admin.register(ContactInfo)
class ContactInfoAdmin(admin.ModelAdmin):
    list_display = ("email", "whatsapp", "telegram", "is_active")
    list_editable = ("is_active",)
    
    def has_add_permission(self, request):
        if ContactInfo.objects.exists():
            return False
        return super().has_add_permission(request)
    
    def changelist_view(self, request, extra_context=None):
        if not ContactInfo.objects.exists():
            ContactInfo.objects.create(
                email="mumoeric19@gmail.com",
                whatsapp="+254758341490",
                telegram="https://t.me/mumoeric",
                is_active=True
            )
            messages.success(request, "Default contact information created. You can edit it below.")
        return super().changelist_view(request, extra_context)
