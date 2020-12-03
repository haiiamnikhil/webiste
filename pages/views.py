from django.shortcuts import render
from .models import *


def Service(request):
    return render(request,'services.html',{'metas':Services.objects.all()})

def Digital_Marking(request):
    return render(request,'digitalmarketing.html',{'metas':DigitalMarking.objects.all()})

def Graphics_Design(request):
    return render(request,'graphicsdesign.html',{'metas':GraphicsDesign.objects.all()})

def Development(request):
    return render(request,'development.html',{'metas':DesignAndDevelopment.objects.all()})

def Website_Design_Development(request):
    return render(request,'websitedesigndevelopment.html',{'metas':WebsiteDesignandDevelopment.objects.all()})

def Mobile_App(request):
    return render(request,'mobileapp.html',{'metas':MobileAppDevelopment.objects.all()})

def About(request):
    return render(request,'about.html',{'metas':AboutUs.objects.all()})

def Our_Package(request):
    return render(request,'ourpackage.html',{'metas':OurPackage.objects.all()})

def Contact(request):
    return render(request,'contact.html',{'metas':ContactUs.objects.all()})