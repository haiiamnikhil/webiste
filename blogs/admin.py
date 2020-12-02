from django.contrib import admin
from .models import Author, Blog,BlogCategory


class BlogList(admin.ModelAdmin):
    list_display = ('title','author','status','published')


admin.site.register(Blog, BlogList)
admin.site.register(Author)
admin.site.register(BlogCategory)
