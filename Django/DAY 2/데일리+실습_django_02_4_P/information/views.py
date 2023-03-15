from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'information/index.html') #2번: templates를 샌드위치 형태로 만들어 주고 경로도 지정해줫음