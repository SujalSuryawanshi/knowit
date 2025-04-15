from django.urls import path
from .views import index, contact
from . import views

urlpatterns = [
    path('', index, name='index'),  # Renders index.html
    path('contact/', contact, name='contact'),  # Renders contact.html
     path('create/', views.create_page, name='create_page'),
    path('page/<int:pk>/', views.view_page, name='view_page'),
    path('posts/', views.page_list, name='page_list'),
    path('search/', views.search, name='search'),  # Search functionality

]
