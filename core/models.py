from django.db import models


class ContactInfo(models.Model):
    email = models.EmailField(max_length=200)
    whatsapp = models.CharField(max_length=20, help_text="e.g. +1234567890")
    telegram = models.URLField(help_text="https://t.me/username")
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = "Contact Info"

    def __str__(self):
        return "Contact Information"


class News(models.Model):
    CATEGORY_CHOICES = [
        ("AI", "AI"),
        ("Forex", "Forex"),
        ("Cybersecurity", "Cybersecurity"),
        ("Emergency", "Emergency"),
    ]

    title = models.CharField(max_length=200)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_emergency = models.BooleanField(default=False)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.title
