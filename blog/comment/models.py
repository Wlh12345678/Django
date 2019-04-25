from django.db import models
from blogtest.models import Post

# Create your models here.

class Comment(models.Model):
    name =models.CharField(max_length=20)
    email = models.EmailField(blank=True,null=True)




