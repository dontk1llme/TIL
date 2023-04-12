# accounts/views.py

@require_POST
def follow(request, user_pk):
    if request.user.is_authenticated:
        person = get_object_or_404(get_user_model(), pk=user_pk)

        if person != request.user:
            if person.followers.filter(pk=request.user.pk).exists():
                person.followers.remove(request.user)
            else:
                person.followers.add(request.user)
        return redirect('accounts:profile', person.username)
    return redirect('accounts:login')


'''
@require_POST
def follow(request, __(a)__):
    if request.user.is_authenticated:
        person = get_object_or_404(get_user_model(), pk=__(a)__)

        if person != request.user:
            if person.__(b)__.__(c)__(pk=request.user.pk).exists():
                person.__(b)__.__(d)__(request.user)
            else:
                person.__(b)__.__(e)__(request.user)
        return redirect('accounts:profile', person.username)
    return redirect('accounts:login')
'''