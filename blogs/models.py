from django.db import models
from taggit.managers import TaggableManager
from PIL import Image
import os


BLOGS_STATUS = (
    (0,'Draft'),
    (1,'Processing'),
    (2,'Live'),
)

class BlogCategory(models.Model):
    postcategory = models.CharField(max_length=100, blank=False, unique=True)

    def __str__(self):
        return self.postcategory

class Author(models.Model):
    name = models.CharField(max_length=50,unique=True,default='Admin')
    email = models.CharField(max_length=50,unique=True)

    def __str__(self):
        return self.name

class Blog(models.Model):
    link = models.SlugField(max_length=256,unique=True)
    blogimage = models.ImageField(upload_to='blogs/')
    title = models.CharField(max_length=256,unique=True)
    selectcategory = models.ForeignKey(to=BlogCategory, on_delete = models.CASCADE)
    author = models.ForeignKey(to=Author,on_delete=models.CASCADE,default='Admin')
    description = models.TextField()
    metta = models.TextField(max_length=256)
    status = models.IntegerField(default=0,choices=BLOGS_STATUS)
    published = models.DateField()
    tags = TaggableManager()

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        image = Image.open(self.blogimage.path)

        if image.height > 100 or image.width > 100:
            new_image = (350,270)
            image.thumbnail(new_image)
            image.save(self.blogimage.path)
