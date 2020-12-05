from django.urls import path, include
from .views import home, About, Our_Package, Contact


urlpatterns = [
    path("",home,name="home"),
    path('about',About,name='aboutus'),
    path('contact',Contact,name='contact'),
    path('ourpackage',Our_Package,name='ourpackage'),
]