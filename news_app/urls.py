from django.urls import path
from .views import index, contact

urlpatterns = [
    path('', index, name='index'),  # Renders index.html
    path('contact/', contact, name='contact'),  # Renders contact.html

]
