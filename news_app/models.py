from django.db import models

class News(models.Model):
    CATEGORY_CHOICES = [
        ('sports', 'Sports'),
        ('politics', 'Politics'),
        ('entertainment', 'Entertainment'),
        ('technology', 'Technology'),
        ('business', 'Business'),
        ('world', 'World'),
    ]
    
    title = models.CharField(max_length=255)
    description = models.TextField()
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    video_url = models.URLField()  # AI-generated video URL
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Post(models.Model):
    title = models.CharField(max_length=255)
    img=models.ImageField(upload_to='posts/', null=True, blank=True)
    img_link=models.TextField(null=True, blank=True)
    affilate_link=models.TextField(null=True, blank=True)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title