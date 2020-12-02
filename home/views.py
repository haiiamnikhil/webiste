from django.shortcuts import render
from .models import Item


def HomePage(request):
    video = Item.objects.all()
    return render(request,'home.html',{'video':video})