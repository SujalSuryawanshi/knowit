from django.shortcuts import render
from django.http import JsonResponse
from .models import News
from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from .forms import CustomPageForm


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



def create_page(request):
    if request.method == 'POST':
        form = CustomPageForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('page_list')
    else:
        form = CustomPageForm()
    return render(request, 'create_page.html', {'form': form})

def view_page(request, pk):
    page = get_object_or_404(Post, pk=pk)
    return render(request, 'page_detail.html', {'page': page})


def page_list(request):
    pages = Post.objects.all()
    return render(request, 'page_list.html', {'pages': pages})

from django.db.models import Q, Count, Avg

def search(request):
    query = request.GET.get('query', '')
    if query:
        pages = Post.objects.filter(
            Q(title__icontains=query)|
            Q(content__icontains=query))
    else:
        pages=Post.objects.none()
    return render(request, 'search_results.html', {'pages': pages, 'query': query})