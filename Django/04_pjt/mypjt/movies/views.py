from django.shortcuts import render, redirect
from .models import Movie
from .forms import MovieForm
from django.views.decorators.http import require_http_methods, require_POST, require_safe

# Create your views here.
@require_http_methods(['GET'])
def index(request):
    movies = Movie.objects.all()
    context = {'movies':movies}
    return render(request, 'movies/index.html', context)

@require_http_methods(['GET'])
def detail(request, pk):
    movie = Movie.objects.get(pk=pk)
    context = {'movie':movie}
    return render(request, 'movies/detail.html', context)

@require_http_methods(['GET','POST'])
def create(request): # new + create
    if request.method == 'POST':
        form = MovieForm(request.POST, request.FILES)
        print(request.FILES)
        print('1')
        if form.is_valid():
            movie = form.save()
            print('2')
            return redirect('movies:detail', movie.pk)
    else:
        print('응안돼')
        form = MovieForm()
    context = {'form':form}
    return render(request, 'movies/create.html', context)

@require_http_methods(['GET','POST'])
def update(request, pk):
    movie = Movie.objects.get(pk=pk)
    if request.method == 'POST':
        form = MovieForm(request.POST, request.FILES, instance=movie)
        if form.is_valid():
            form.save()
            return redirect('movie:detail', pk=movie.pk)
    else:
        form = MovieForm(instance=movie)
    context = {'form':form, 'movie':movie}
    return render(request, 'movies/update.html',context)

#post만 허용하라고 하는데 여기에서 get을 해야되는데 어쩌라는거임 걍 안함
def delete(request, pk):
    movie = Movie.objects.get(pk=pk)
    movie.delete()
    return redirect('movies:index')