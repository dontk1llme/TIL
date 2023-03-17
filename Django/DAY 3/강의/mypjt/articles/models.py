from django.db import models

# Create your models here.
class Article(models.Model):
    title=models.CharField(max_length=10) #char이라서 명시해줘야함
    content=models.TextField()

#id칼럼은 테이블 생성 시 django가 자동으로 생성