from django.db import models

# Create your models here.

class Recipedb(models.Model):
    recipename=models.CharField(max_length=50)
    image=models.ImageField(upload_to='recipe',default="null.jpg")
    instraction=models.TextField(default=0)
    ingredients=models.TextField(default=0)