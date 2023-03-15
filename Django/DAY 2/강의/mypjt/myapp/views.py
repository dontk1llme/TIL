from django.shortcuts import render

# Create your views here.
def index(request):
    info = {
        'name' : 'seuri',
        'age' : '24',

    }
    return render(request, 'myapp/index.html', {'info':info})


