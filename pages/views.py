from django.shortcuts import render
from .models import *


def Service(request):
    return render(
        request,'services.html',
        {
            'metas':Services.objects.all()
        })

def Digital_Marking(request):
    return render(
        request,'services/digitalmarketing.html',
        {
            'metas':DigitalMarking.objects.all()
        })

def GraphicsDesignAndMultimedia(request):
    return render(
        request,'services/graphicsdesignandmultimedia.html',
        {
            'metas':GraphicsDesign.objects.all()
        })

def DesignAnd_Development(request):
    return render(
        request,'designanddevelopment.html',
        {
            'metas':DesignAndDevelopment.objects.all()
        })

def WebsiteDesignand_Development(request):
    return render(
        request,'services/websitedesignanddevelopment.html',
        {
            'metas':WebsiteDesignandDevelopment.objects.all()
        })

def Mobile_App(request):
    return render(
        request,'services/mobileappdevelopment.html',
        {
            'metas':MobileAppDevelopment.objects.all()
        })

def SearchEngineOptimization(request):
    return render(
        request,'services/mobileappdevelopment.html',
        {
            'metas':SEO.objects.all()
        })

def SocialMediaOptimization(request):
    return render(
        request,'services/mobileappdevelopment.html',
        {
            'metas':SMO.objects.all()
        })

def EmailMarketing(request):
    return render(
        request,'services/mobileappdevelopment.html',
        {
            'metas':EM.objects.all()
        })

def ContentMarketing(request):
    return render(
        request,'services/mobileappdevelopment.html',
        {
            'metas':CM.objects.all()
        })

def PayPerClickMarketing(request):
    return render(
        request,'services/mobileappdevelopment.html',
        {
            'metas':PPCM.objects.all()
        })

def BrandMarketing(request):
    return render(
        request,'services/mobileappdevelopment.html',
        {
            'metas':Branding.objects.all()
        })

