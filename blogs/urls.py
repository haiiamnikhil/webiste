from django.urls import path
from .views import ListPage, BlogDetailPage


urlpatterns = [
    path('',ListPage,name='blogs'),
    path('<slug:link>',BlogDetailPage,name='BlogDetailPage'),
]