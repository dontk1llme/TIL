from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'articles/index.html')

def throw(request): #데이터 보내기
    return render(request, 'articles/throw.html')

def catch(request): #데이터 잡기
    message = request.GET.get('message')
    context = {
        'message' : message
    }
    return render(request, 'articles/catch.html', context)