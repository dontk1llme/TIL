# c- serializers.py
# https://5-ssssseung.tistory.com/89


class ArticleSerializer(serializers.ModelSerializer):
    # __(c)__ = serializers.IntegerField(
    #     __(a)__='__(b)__',
    #     read_only=True,
    # )

    comment_count = serializers.IntegerField(
        source='comment_set.count', #comment_set은 자동으로 구성 가능
        read_only=True, 
    )

    class Meta:
        model = Article
        fields = ('id', 'title', 'content', 'created_at', 'updated_at', 'comment_count',)