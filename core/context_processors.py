from .models import News

def emergency_news(request):
    return {
        'emergency_items': News.objects.filter(is_emergency=True)
    }
