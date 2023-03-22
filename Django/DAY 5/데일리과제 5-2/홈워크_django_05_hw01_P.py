# def create(request):
#     if request.method == "POST":
#         form = ArticleForm(request.POST)
#         if form.is_valid():
#             title = form.__(a)__
#             content = form.__(b)__
#             article = Article(title=title,content=content)
#             __(c)__
#             return redirect('articles:detail',article.pk)
#     form = ArticleForm()
#     context = {
#         'form':form
#     }
#     return render(request,'articles/create.html',context)

def create(request):
    if request.method == "POST":
        form = ArticleForm(request.POST)
        if form.is_valid():
            #form.cleaned_data는 좀 다름! 통과된 애만 들어옴
            cleaned_data = form.cleaned_data
            title = form.cleaned_data.get('title')
            content = form.cleaned_data.get('content')
            article = Article(title=title,content=content)
            article.save()
            return redirect('articles:detail',article.pk)
    form = ArticleForm()
    context = {
        'form':form
    }
    return render(request,'articles/create.html',context)