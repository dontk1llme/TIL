from django.db import models
from django.forms.widgets import TextInput


# Create your models here.

class NumberInput(TextInput):
    input_type='number'

class Movie(models.Model):
    title = models.CharField(max_length=20) #영화 제목
    audience = models.IntegerField()#관객 수
    release_date = models.DateField() #개봉일
    
    genre_choice = (('comedy','코미디'), ('horror','공포'), ('romance','로맨스'))
    genre = models.CharField(max_length=30, choices=genre_choice) #장르

    score = models.FloatField() #평점
    poster_url = models.CharField(max_length=50) #포스터 경로
    description = models.TextField() #줄거리
    actor_image = models.ImageField() #대표 배우 이미지


