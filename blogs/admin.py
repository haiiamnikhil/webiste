from django.contrib import admin
from .models import Author, Blog,BlogCategory, BlogListingPage


class BlogList(admin.ModelAdmin):
    list_display = ('title','author','category','status','published')


admin.site.register(BlogListingPage)
admin.site.register(Blog, BlogList)
admin.site.register(Author)
admin.site.register(BlogCategory)
