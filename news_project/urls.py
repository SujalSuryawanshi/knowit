from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from news_project import settings
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('news_app.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_URL)
urlpatterns += staticfiles_urlpatterns()
