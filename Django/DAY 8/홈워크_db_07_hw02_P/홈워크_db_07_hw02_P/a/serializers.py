# a- serializers.py

class ArticleListSerializer(serializers.ModelSerializer): #get

    class Meta:
        model = Article
        # fields = __(d)__
        fields = ('id','title') 


class ArticleSerializer(serializers.ModelSerializer): #post

    class Meta:
        model = Article
        # fields = __(e)__
        fields = ('id','title','created_at', 'updated_at') 