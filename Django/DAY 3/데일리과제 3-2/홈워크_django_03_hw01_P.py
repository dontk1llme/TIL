#  'title', 'content' 필드를 가지고 있는 Article model 

from django.db import models

# Create your models here.
class Article(models.Model):
    title=models.CharField(max_length=15) #char이라서 명시해줘야함
    content=models.TextField()