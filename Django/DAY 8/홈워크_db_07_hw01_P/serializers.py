from rest_framework import serializers
from .serializers import Article


# class ArticleSerializer(__(b)__):
class ArticleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Article
        fields = '__all__'