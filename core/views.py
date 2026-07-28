from django.shortcuts import render

def home(request):

    breaking_news = [
        {
            "title": "OpenAI releases a new AI model",
            "category": "AI",
        },
        {
            "title": "Gold price climbs as USD weakens",
            "category": "Forex",
        },
        {
            "title": "Critical Windows security vulnerability discovered",
            "category": "Cybersecurity",
        },
    ]

    return render(request, "home.html", {
        "breaking_news": breaking_news
    })