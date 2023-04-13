from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import render
from django.http.response import JsonResponse, HttpResponse #######
from django.core import serializers #####
from .models import Article
from .serializers import ArticleSerializer ####

# Create your views here.
def article_html(request): #HTML 사용
    articles = Article.objects.all()
    context = {'articles': articles}
    return render(request, 'articles/article.html', context)


def article_json_1(request): #JsonResponse()를 사용
    articles = Article.objects.all()
    articles_json = [] #교재에 {}돼있는데 append 쓰려고 []로
    for article in articles:
        articles_json.append({
            'id': article.pk,
            'title': article.title,
            'content':article.content,
        })
    return JsonResponse(articles_json, safe=False)


def article_json_2(request): #Django Serializer 사용
    articles = Article.objects.all()
    data = serializers.serialize('json', articles)
    return HttpResponse(data, content_type='application/json')


@api_view(['GET']) #DRF는 데코레이터 필수
def article_json_3(request): #Django REST Framework (DRF) 사용
    articles = Article.objects.all()
    serializer = ArticleSerializer(articles, many = True)
    return Response(serializer.data)

###########################################################################
#DRF
# http://127.0.0.1:8000/api/v1/articles
# 참고: (_가 - 됨 url에서는)
@api_view(['GET'])
def article_list(request):
    articles = Article.objects.all()
    serializer = ArticleSerializer(articles, many=True) #many: 여러개
    return Response(serializer.data)

@api_view(['GET'])
def article_detail(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    serializer = ArticleSerializer(article)
    return Response(serializer.data)