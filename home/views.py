from django.shortcuts import render
from .models import HomePage


def home(request):
    pagecontent = HomePage.objects.get()
    return render(request,'home.html',context={'metatitle':pagecontent})