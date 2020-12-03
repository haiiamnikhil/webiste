from hashengines.settings import MEDIA_ROOT
from django.shortcuts import render
from .models import Blog, BlogCategory


def ListPage(request):
    latest = Blog.objects.filter(status=2).order_by('-published')[0:1]
    pasttwopost = Blog.objects.filter(status=2).order_by('-published')[1:3]
    recentpost = Blog.objects.filter(status=2).order_by('-published')[0:5]
    blogs = Blog.objects.filter(status=2).order_by('-published')

    tags = [tag for tag in Blog.tags.get_queryset() if tag is not None]
    categories = BlogCategory.objects.all()
    return render(request,'blog.html',{'metatitle':'HashEngines Blog','blogs':blogs,'latest':latest,'media':MEDIA_ROOT,'categories':categories,'pasttwopost':pasttwopost,'recentpost':recentpost})


def BlogDetailPage(request,link):

    getBlog = Blog.objects.filter(link=link)
    tags = [tag for tag in Blog.objects.all() if tag is not None]
    Blog.objects.filter(link=link)[0]
    return render(request,'bloglist.html',context={'blog':getBlog,'tags':tags,'metatitle':Blog.objects.filter(link=link)[0]})