from django.db import models

class UserInformations(models.Model):
    name = models.CharField(max_length=50,unique=True,blank=False)
    email = models.EmailField(blank=False,max_length=50,unique=True)
    emp_no = models.IntegerField()
    password = models.CharField(blank=False,max_length=50)

    def __str__(self):
        return self.name