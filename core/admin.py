from django.contrib import admin
from django.contrib import messages
from django.shortcuts import redirect
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
    
    def has_add_permission(self, request):
        # Prevent adding more than one ContactInfo entry
        if ContactInfo.objects.exists():
            return False
        return super().has_add_permission(request)
    
    def changelist_view(self, request, extra_context=None):
        if not ContactInfo.objects.exists():
            # Auto-create default contact info if none exists
            ContactInfo.objects.create(
                email="mumoeric19@gmail.com",
                whatsapp="+254758341490",
                telegram="https://t.me/mumoeric",
                is_active=True
            )
            messages.success(request, "Default contact information created. You can edit it below.")
        return super().changelist_view(request, extra_context)
