from django.db import models
# from embed_video.fields import EmbedVideoField

class HomePage(models.Model):
    metatitle = models.TextField(max_length=256,blank=False)
    metadescription = models.TextField(max_length=256,blank=False)
    metakeywords = models.TextField(max_length=256,blank=True,unique=False)

    def __str__(self):
        return self.metatitle