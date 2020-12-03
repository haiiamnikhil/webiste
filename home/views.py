from django.shortcuts import render
from .models import HomePage


def home(request):
    return render(
        request,'home.html',
        {
            'metas':HomePage.objects.all()
        }
        )