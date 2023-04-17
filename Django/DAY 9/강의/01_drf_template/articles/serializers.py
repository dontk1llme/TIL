from rest_framework import serializers
from .models import Article, Comment


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields=('article',) #해당 필드 유효성 검사 ㄴㄴ 조회 시에는 출력 ㅇㅇ

    def to_representation(self, instance):
        rep= super().to_representation(instance)
        rep.pop('article',None) #article 보여주지마!
        return rep

class ArticleListSerializer(serializers.ModelSerializer):
    # comment_set = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    comment_set = CommentSerializer(many=True, read_only=True)
    comment_count = serializers.IntegerField(source = 'comment_set.count', read_only=True)

    class Meta:
        model = Article
        fields = ('id', 'title', 'content','comment_set', 'comment_count',)
        # fields ='__all__'

    def to_representation(self, instance): #보여줄때만 pop! 
        rep= super().to_representation(instance)
        rep['comments']=rep.pop('comment_set', []) #잇으면 comment_set 넘기기, 없으면 []
        return rep

