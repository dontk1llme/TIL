# from rest_framework import serializers
# from .models import (__(a)__)


# class ArticleSerializer(__(b)__):

#     class Meta:
#         model = Article
#         fields = (__(c)__) # 개별 필드를 나열하지 말 것

from rest_framework import serializers
from .models import Article


class ArticleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Article
        fields = ('__all__') # 개별 필드를 나열하지 말 것

