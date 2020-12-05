from django.shortcuts import render
from .models import HomePage
from blogs.models import Blog
from pages.models import AboutUs, OurPackage, ContactUs

def home(request):
    return render(
        request,'home.html',
        {
            'metas':HomePage.objects.all(),
            'latestBlogs':Blog.objects.filter(status=2).order_by('-published')[0:3]
        })

def About(request):
    return render(
        request,'about.html',
        {
            'metas':AboutUs.objects.all()
        })

def Our_Package(request):
    return render(
        request,'ourpackage.html',
        {
            'metas':OurPackage.objects.all()
        })

def Contact(request):
    return render(
        request,'contact.html',
        {
            'metas':ContactUs.objects.all()
        })