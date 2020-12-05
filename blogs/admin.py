from django.contrib import admin
from .models import Author, Blog,BlogCategory, BlogListingPage, AddImage


class BlogList(admin.ModelAdmin):
    list_display = ('title','author','category','status','published')

class PostImageAdmin(admin.StackedInline):
    model = AddImage

admin.site.register(BlogListingPage)
admin.site.register(AddImage)
admin.site.register(Blog, BlogList)
admin.site.register(Author)
admin.site.register(BlogCategory)
