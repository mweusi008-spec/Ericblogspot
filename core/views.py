from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.utils import timezone
import requests
import feedparser
from .models import News, ContactInfo


def _fetch_feed(url, limit=20):
    articles = []
    try:
        feed = feedparser.parse(url)
        for entry in feed.entries[:limit]:
            published = entry.get("published", "")
            if published:
                try:
                    from datetime import datetime
                    import email.utils
                    dt = datetime(*entry.published_parsed[:6])
                    published = dt.strftime("%b %d, %Y")
                except Exception:
                    pass
            
            articles.append({
                "title": entry.get("title", "No title"),
                "link": entry.get("link", "#"),
                "published": published,
                "summary": entry.get("summary", "")[:200],
                "source": "RSS",
            })
    except Exception:
        pass
    return articles


def home(request):
    rss_articles = []
    rss_feeds = [
        "https://www.standardmedia.co.ke/rss/headlines.php",
        "https://www.standardmedia.co.ke/rss/kenya.php",
        "https://www.standardmedia.co.ke/rss/politics.php",
        "https://www.bbc.com/news/entertainment_and_arts/rss.xml",
        "https://www.tmz.com/rss.xml",
    ]
    
    for feed_url in rss_feeds:
        rss_articles.extend(_fetch_feed(feed_url, limit=10))
    
    rss_articles.sort(key=lambda x: x.get("published", ""), reverse=True)
    rss_articles = rss_articles[:20]

    return render(request, "home.html", {
        "rss_articles": rss_articles,
    })


def news_detail(request, pk):
    news = get_object_or_404(News, pk=pk)
    return render(request, "news_detail.html", {"news": news})


def ai_news(request):
    articles = _fetch_feed("https://techcrunch.com/category/artificial-intelligence/feed/", limit=30)
    return render(request, "ai_news.html", {
        "articles": articles,
        "title": "AI News",
        "last_updated": timezone.now(),
    })


def cybersecurity_news(request):
    articles = _fetch_feed("https://feeds.feedburner.com/TheHackersNews", limit=30)
    return render(request, "cybersecurity_news.html", {
        "articles": articles,
        "title": "Cybersecurity News",
        "last_updated": timezone.now(),
    })


def emergency_news(request):
    emergency_items = News.objects.filter(is_emergency=True)
    return render(request, "emergency_news.html", {
        "emergency_items": emergency_items,
        "last_updated": timezone.now(),
    })


def forex_news(request):
    rates = {}
    gold_price = None
    gold_error = None
    error = None

    try:
        rate_resp = requests.get(
            "https://open.er-api.com/v6/latest/USD",
            timeout=10
        )
        if rate_resp.status_code == 200:
            data = rate_resp.json()
            rates = data.get("rates", {})
            rates = {
                k: v for k, v in rates.items()
                if k in ["EUR", "GBP", "JPY", "CHF", "AUD", "CAD", "NZD"]
            }
        else:
            error = "Failed to fetch exchange rates."
    except Exception:
        error = "Error connecting to exchange rate service."

    try:
        gold_resp = requests.get(
            "https://api.gold-api.com/price/XAU",
            timeout=10
        )
        if gold_resp.status_code == 200:
            gold_data = gold_resp.json()
            gold_price = gold_data.get("price")
    except Exception:
        gold_error = "Error fetching gold price."

    forex_articles = _fetch_feed("https://www.forexlive.com/feed/news", limit=30)

    return render(request, "forex.html", {
        "rates": rates,
        "gold_price": gold_price,
        "gold_error": gold_error,
        "forex_articles": forex_articles,
        "error": error,
        "last_updated": timezone.now(),
    })


def news_api(request):
    category = request.GET.get("category")
    if category:
        items = News.objects.filter(category=category)
    else:
        items = News.objects.all()
    data = [
        {
            "title": n.title,
            "category": n.category,
            "content": n.content,
            "created_at": n.created_at.isoformat(),
            "is_emergency": n.is_emergency,
        }
        for n in items
    ]
    return JsonResponse({"news": data})


def emergency_api(request):
    items = News.objects.filter(is_emergency=True)
    data = [
        {
            "title": n.title,
            "content": n.content,
            "created_at": n.created_at.isoformat(),
        }
        for n in items
    ]
    return JsonResponse({"emergency": data})


def contact(request):
    contact_info = ContactInfo.objects.filter(is_active=True).order_by('-id').first()
    return render(request, "contact.html", {
        "contact_info": contact_info,
    })


def setup_admin(request):
    from django.contrib.auth import get_user_model
    User = get_user_model()
    
    if User.objects.filter(username='admin').exists():
        return render(request, "setup_admin.html", {
            "status": "exists",
            "message": "Admin user already exists."
        })
    
    User.objects.create_superuser('admin', 'admin@ericblogspot.com', 'admin123')
    return render(request, "setup_admin.html", {
        "status": "success",
        "message": "Admin user created! Username: admin, Password: admin123"
    })
