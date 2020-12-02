from hashengines.settings import MEDIA_ROOT
from django.shortcuts import render
from .models import Blog
from bs4 import BeautifulSoup


def ListPage(request):
    blogs = Blog.objects.filter(status=2).order_by('-published')
    latest = Blog.objects.filter(status=2).order_by('-published')[0:5]

    tags = [tag for tag in Blog.tags.get_queryset() if tag is not None]

    return render(request,'blog.html',{'blogs':blogs,'latest':latest,'media':MEDIA_ROOT})


def BlogDetailPage(request,link):

    getBlog = Blog.objects.filter(link=link)
    tags = [tag for tag in Blog.objects.all() if tag is not None]

    return render(request,'bloglist.html',context={'blog':getBlog,'tags':tags})