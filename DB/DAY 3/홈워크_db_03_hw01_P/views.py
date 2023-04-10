# views.py
# def detail(request, __(a)__):
def detail(request, pk):
    article = get_object_or_404(Article, pk=article_pk)

    comment_form = CommentForm()
    context_data = {
        'article': article,
        # __(b)__,
        'comment_form':comment_form,
    }
    # return render(request, 'eithers/detail.html', __(c)__)
    return render(request, 'eithers/detail.html', context_data)