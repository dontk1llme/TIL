from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
#
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm
from .forms import CustomUserChangeForm, CustomUserCreationForm
#
from django.views.decorators.http import require_http_methods, require_POST, require_safe


# Create your views here.
def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('articles:index')
    else:
        form = AuthenticationForm()

    context = {'form': form}
    return render(request, 'accounts/login.html', context)

def logout(request):
    auth_logout(request)
    return redirect('articles:index')

def signup(request):
    if request.method=='POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            #form.save()
            user = form.save()
            auth_login(request, user) #이렇게 해둬야 회원가입하면 바로 로그인댐
            return redirect('articles:index')
    else: 
        form = CustomUserCreationForm()
    context = {'form':form}
    return render(request, 'accounts/signup.html', context)

@require_http_methods(['GET','POST'])
def delete(request):
    user = request.user
    user.delete() #삭제 후
    auth_logout(request) #로그아웃! 순서 중요
    return redirect('articles:index')

@require_POST
def update(request):
    if request.method=='POST':
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('articles:index')
    else:
        form = CustomUserChangeForm(instance=request.user)
    context={'form':form}
    return render(request, 'accounts/update.html', context)

@require_safe #<-GET보다는 얘 권장! 오류 안 뜨게 하는 방향으루
def change_password(request):
    if request.method=='POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user) #얘가 잇어야 비밀번호 유지
            return redirect('articles:index')
    else:
        form = PasswordChangeForm(request.user)
    context = {'form':form,}
    return render(request, 'accounts/change_password.html', context)