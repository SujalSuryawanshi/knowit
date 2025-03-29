from django.shortcuts import render
from django.http import JsonResponse
from .models import News

# Function to return the frontend page
def index(request):
    return render(request, 'index.html')

def contact(request):
    return render(request, 'contact.html')
# API to return news in JSON format
def get_news(request):
    category = request.GET.get('category', 'all')

    if category == "all":
        news_list = News.objects.all().order_by('-timestamp')
    else:
        news_list = News.objects.filter(category=category).order_by('-timestamp')

    news_data = [
        {
            "title": news.title, 
            "description": news.description, 
            "video_url": news.video_url,
            "category": news.category
        }
        for news in news_list
    ]

    return JsonResponse({"news": news_data})

