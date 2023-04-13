# a- views.py
# https://ssungkang.tistory.com/entry/Django-Serializer-%EB%A5%BC-%ED%86%B5%ED%95%9C-%EC%9C%A0%ED%9A%A8%EC%84%B1-%EA%B2%80%EC%82%AC-%EB%B0%8F-%EC%A0%80%EC%9E%A5


from rest_framework import status
from .models import Article

@api_view(['GET', 'POST'])
def article_list_create(request):
    if request.method == 'GET':
        articles = Article.objects.all()
        serializer = ArticleListSerializer(articles, many=True)
        return Response(serializer.data)
    else: #POST
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        # if serializer.is_valid(__(a)__):
        #     serializer.__(b)__ 
        #     return Response(serializer.data, status=__(c)__)