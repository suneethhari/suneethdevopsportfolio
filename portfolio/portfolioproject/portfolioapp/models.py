from django.db import models

# Create your models here.
class Contactform(models.Model):
    name=models.CharField(max_length=250)
    email=models.TextField()
    subject=models.CharField(max_length=250)
    msg=models.CharField(max_length=1000)