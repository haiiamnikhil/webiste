from django.db import models

class Services(models.Model):
    metatitle = models.TextField(max_length=60,blank=False)
    metadescription = models.TextField(max_length=250, blank=False)
    metakeywords = models.TextField(max_length=256,blank=True)

    def __str__(self):
        return self.metatitle


class DigitalMarking(models.Model):
    metatitle = models.TextField(max_length=60,blank=False)
    metadescription = models.TextField(max_length=250, blank=False)
    metakeywords = models.TextField(max_length=256,blank=True)

    def __str__(self):
        return self.metatitle

class GraphicsDesign(models.Model):
    metatitle = models.TextField(max_length=60,blank=False)
    metadescription = models.TextField(max_length=250, blank=False)
    metakeywords = models.TextField(max_length=256,blank=True)

    def __str__(self):
        return self.metatitle

class DesignAndDevelopment(models.Model):
    metatitle = models.TextField(max_length=60,blank=False)
    metadescription = models.TextField(max_length=250, blank=False)
    metakeywords = models.TextField(max_length=256,blank=True)

    def __str__(self):
        return self.metatitle

class WebsiteDesignandDevelopment(models.Model):
    metatitle = models.TextField(max_length=60,blank=False)
    metadescription = models.TextField(max_length=250, blank=False)
    metakeywords = models.TextField(max_length=256,blank=True)

    def __str__(self):
        return self.metatitle


class MobileAppDevelopment(models.Model):
    metatitle = models.TextField(max_length=60,blank=False)
    metadescription = models.TextField(max_length=250, blank=False)
    metakeywords = models.TextField(max_length=256,blank=True)

    def __str__(self):
        return self.metatitle

class AboutUs(models.Model):
    metatitle = models.TextField(max_length=60,blank=False)
    metadescription = models.TextField(max_length=250, blank=False)
    metakeywords = models.TextField(max_length=256,blank=True)

    def __str__(self):
        return self.metatitle


class OurPackage(models.Model):
    metatitle = models.TextField(max_length=60,blank=False)
    metadescription = models.TextField(max_length=250, blank=False)
    metakeywords = models.TextField(max_length=256,blank=True)

    def __str__(self):
        return self.metatitle


class ContactUs(models.Model):
    metatitle = models.TextField(max_length=60,blank=False)
    metadescription = models.TextField(max_length=250, blank=False)
    metakeywords = models.TextField(max_length=256,blank=True)

    def __str__(self):
        return self.metatitle