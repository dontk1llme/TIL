# b- serializers.py
# https://velog.io/@hsngju/DRF-03-CRUD-%EC%A0%81%EC%9A%A9
# https://wisdom-990629.tistory.com/entry/DRF-%EB%8C%93%EA%B8%80-%EA%B8%B0%EB%8A%A5-%EA%B5%AC%ED%98%84%ED%95%98%EA%B8%B0
# 문제를 왜이렇게 해놧어?!
# https://www.django-rest-framework.org/api-guide/relations/

# commentserializer 없이 이게 되는게 말이안댐... ㄱ-


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ('id','content','article',)


class ArticleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Article
        fields = ('id', 'title', 'content', 'created_at', 'updated_at', 'comment_set')

# class ArticleSerializer(serializers.ModelSerializer):
#     __(b)__ = __(a)__(
#         __(c)__,
#         __(d)__,
#     )

#     class Meta:
#         model = Article
#         fields = ('id', 'title', 'content', 'created_at', 'updated_at', '__(b)__')