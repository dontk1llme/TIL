from .serializers import ArticleSerializer
from rest_framework.response import Response
from .serializers import Article

@api_view(['GET'])
def article_list(request):
    articles = Article.objects.all()
    serializer = ArticleSerializer(articles, many=True)
    return Response(serializer.data)


# from .serializers import __(a)__
# from rest_framework.response import __(d)__
# from .serializers import Article

# @api_view(['GET'])
# def article_list(request):
#     articles = Article.objects.all()
#     serializer = __(a)__(articles, __(c)__)
#     return __(d)__(serializer.__(e)__)