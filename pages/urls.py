from django.urls import path
from .views import *

urlpatterns = [
    path('',Service,name='service'),
    path('digital-marketing',Digital_Marking,name='digital_marketing'),
    path('graphics-design-and-multimedia',GraphicsDesignAndMultimedia,name='graphics_design'),
    path('website-development-company',DesignAnd_Development,name='designanddevelopment'),
    path('wordpress-website-development',WebsiteDesignand_Development,name='website_design_development'),
    path('mobile-app-development',Mobile_App,name='mobile_app'),
    path('search-engine-optimization',SearchEngineOptimization,name='seo'),
    path('social-media-optimization',SocialMediaOptimization,name='smo'),
    path('email-marketing',EmailMarketing,name='emailmarketing'),
    path('content-marketing',ContentMarketing,name='contentmarketing'),
    path('pay-per-click-marketing',PayPerClickMarketing,name='ppcm'),
    path('branding',BrandMarketing,name='branding'),
]