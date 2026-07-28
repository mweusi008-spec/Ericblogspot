from django.urls import path
from .views import home, news_detail, forex_news, ai_news, cybersecurity_news, emergency_news, news_api

urlpatterns = [
    path('', home, name='home'),
    path('news/<int:pk>/', news_detail, name='news_detail'),
    path('forex/', forex_news, name='forex'),
    path('ai-news/', ai_news, name='ai_news'),
    path('cybersecurity/', cybersecurity_news, name='cybersecurity'),
    path('emergency/', emergency_news, name='emergency'),
    path('api/news/', news_api, name='news_api'),
]