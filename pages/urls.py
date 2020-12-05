from django.urls import path
from .views import *

urlpatterns = [
    path('',Service,name='service'),
    path('digital-marketing',Digital_Marking,name='digital_marketing'),
    path('graphics-design-and-multimedia',Graphics_Design,name='graphics_design'),
    path('website-development-company',Development,name='websitedesignanddevelopment'),
    path('wordpress-website-development',Website_Design_Development,name='website_design_development'),
    path('mobile-app-development',Mobile_App,name='mobile_app'),
]