from django.db import models

# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=15)
    content = models.TextField()    

    created_at = models.DateTimeField(auto_now_add=True) #더해질때(add) 값
    updated_at = models.DateTimeField(auto_now=True) #변경될 때마다 now

    def __str__(self):
        return f'{self.id}번 글 - {self.title}:{self.content}'