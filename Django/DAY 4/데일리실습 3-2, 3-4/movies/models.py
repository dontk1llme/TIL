from django.db import models

# Create your models here.

class Movie(models.Model):
    title = models.CharField(max_length=15)
    genre = models.TextField()    
    director=models.CharField(default='Unknown', max_length=20) #default 설정 안하면 에러

    def __str__(self):
        return f'{self.id}번째 영화 - {self.title}({self.genre})'