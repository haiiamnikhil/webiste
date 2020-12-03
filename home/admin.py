from django.contrib import admin
from embed_video.admin import AdminVideoMixin
from .models import HomePage

class MyModelAdmin(admin.ModelAdmin):
    list_display = ('metatitle','metadescription','metakeywords')

admin.site.register(HomePage, MyModelAdmin)