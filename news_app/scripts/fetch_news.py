import requests
from news_app.models import News

def fetch_news():
    api_key = "a6c63111500640719a9045e08c38821f"
    url = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={api_key}"
    response = requests.get(url).json()

    for article in response['articles']:
        News.objects.create(
            title=article['title'],
            description=article['description'],
            category='world',
            video_url='https://example.com/generated-video.mp4'  # Placeholder for AI-generated video
        )
