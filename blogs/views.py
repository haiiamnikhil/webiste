from hashengines.settings import MEDIA_ROOT
from django.shortcuts import render
from .models import Blog, BlogCategory, BlogListingPage


def ListPage(request):
    latest = Blog.objects.filter(status=2).order_by('-published')[0:1]
    pasttwopost = Blog.objects.filter(status=2).order_by('-published')[1:3]
    recentpost = Blog.objects.filter(status=2).order_by('-published')[0:5]
    blogs = Blog.objects.filter(status=2).order_by('-published')[3:]

    tags = [tag for tag in Blog.tags.get_queryset() if tag is not None]
    categories = BlogCategory.objects.all()
    return render(
        request,'blog.html',
        {
            'metas':BlogListingPage.objects.all(),
            'blogs':blogs,
            'latest':latest,
            'media':MEDIA_ROOT,
            'categories':categories,
            'pasttwopost':pasttwopost,
            'recentpost':recentpost
        }
        )


def BlogDetailPage(request,link):

    getBlog = Blog.objects.filter(link=link)
    tags = [tag for tag in Blog.objects.all() if tag is not None]
    categories = BlogCategory.objects.all()
    recentpost = Blog.objects.filter(status=2).order_by('-published')[0:5]
    return render(
        request,'blogdetailpage.html',
        {
            'blog':getBlog,
            'categories':categories,
            'recentpost':recentpost,
            'tags':tags,
            'metatitle':Blog.objects.filter(link=link)[0]
        }
        )