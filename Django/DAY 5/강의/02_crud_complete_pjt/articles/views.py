from django.shortcuts import render, redirect
from .models import Article
from .forms import ArticleForm

# Create your views here.
def index(request):
    articles = Article.objects.all()
    context = {'articles': articles}
    return render(request, 'articles/index.html', context)


def detail(request, pk):
    article = Article.objects.get(pk=pk)
    context = {'article': article}
    return render(request, 'articles/detail.html', context)


def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save()
            return redirect('articles:detail', article.pk)
        # title = request.POST.get('title')
        # content = request.POST.get('content')
        # article = Article(title=title, content=content)
        # article.save()
        # return redirect('articles:create')
    else:
        form = ArticleForm()
    #중복되는 코드 정리. . .    
    context = {'form':form}
    return render(request, 'articles/create.html',context)


def delete(request, pk):
    article = Article.objects.get(pk=pk)
    article.delete()
    return redirect('articles:index')


def update(request, pk):
    article = Article.objects.get(pk=pk)
    if request.method == 'POST':
        form = ArticleForm(request.POST, instance = article) #위위줄 아티클
        if form.is_valid():
            form.save()
            return redirect('article:detail', pk=article.pk)

        # article.title = request.POST.get('title')
        # article.content = request.POST.get('content')
        # article.save()
        # return redirect('articles:detail', pk=article.pk)
    else:
        form = ArticleForm(instance=article)
    context = {'article': article}
    return render(request, 'articles/update.html', context)
