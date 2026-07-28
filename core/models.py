from django.db import models


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
