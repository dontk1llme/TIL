def detail(request, question_pk):
    question = get_object_or_404(Question, pk=question_pk)

    comment_form = CommentForm()

    count_a = question.comment_set.filter(pick=False).count()
    count_b = question.comment_set.filter(pick=True).count()
    total_count = count_a+count_b

    per_a = 0
    per_b = 0
    if comment_form.is_valid():
        per_a = round(count_a / total_count * 100, 1) #소수점 첫 번쨰
        per_b = round(count_b / total_count * 100, 1)

    comments = question.comment_set.all()
    context = {
        'question': question,
        'comment_form': comment_form,
        'count_a': count_a,
        'count_b': count_b,
        'per_a': per_a,
        'per_b': per_b,
        'comments': comments,
    }
    return render(request, 'eithers/detail.html', context)


# 문제
# 댓글의 갯수와 각 종류별로 몇 % 에 해당하는지 계산을 하고자 할 때, 다음 빈 칸에 들어갈 알맞은 코드를 작성하시오. 
# 이 때 %는 소수점 첫 번째자리까지 나타내고 댓글의 순서는 최근에 작성한 댓글 순서로 나타날 수 있게 정렬하시오.

#object로 생각
# https://docs.djangoproject.com/en/4.2/ref/models/querysets/
# https://gaussian37.github.io/python-django-django-query-set/

# 원문
# def detail(request, question_pk):
#     question = get_object_or_404(Question, pk=question_pk)

#     comment_form = CommentForm()

#     count_a = question.comment_set.filter(pick=False).__(a)__
#     count_b = question.comment_set.filter(pick=True).__(a)__
#     total_count = __(b)__

#     per_a = 0
#     per_b = 0
#     if __(c)__:
#         per_a = round(count_a / total_count * 100, __(d)__)
#         per_b = round(count_b / total_count * 100, __(d)__)

#     comments = question.comment_set.__(e)__
#     context = {
#         'question': question,
#         'comment_form': comment_form,
#         'count_a': count_a,
#         'count_b': count_b,
#         'per_a': per_a,
#         'per_b': per_b,
#         'comments': comments,
#     }
#     return render(request, 'eithers/detail.html', context)