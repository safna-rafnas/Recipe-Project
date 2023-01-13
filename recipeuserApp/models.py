from django.db import models

# Create your models here.
class Contactdb (models.Model):
    message=models.TextField()
    name=models.CharField(max_length=50)
    email=models.EmailField()
    subject=models.TextField()
class Registerdb (models.Model):
    username=models.CharField(max_length=50)
    password=models.CharField(max_length=50)
    email=models.EmailField()
    phone=models.IntegerField()
