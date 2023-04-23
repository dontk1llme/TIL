from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods, require_POST, require_safe
from .models import Item
from .forms import ItemForm


@require_safe
def index(request):
    items = Item.objects.all()
    context = {
        'items': items,
    }
    return render(request, 'shops/index.html', context)

# 문제 5. 글을 생성하면 발생하는 에러를 수정하여 detail 페이지로 이동하도록 하시오.
@require_http_methods(['GET', 'POST'])
def create(request):
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            item = form.save()
            # return redirect('shops:detail')
            return redirect('shops:detail', item.pk) #item.pk 추가
    else:
        form = ItemForm()

    context = {
        'form': form,
    }
    return render(request, 'shops/create.html', context)


@require_safe
def detail(request, pk):
    item = Item.objects.get(pk=pk)
    context = {
        'item': item,
    }
    return render(request, 'shops/detail.html', context)


# 문제 6. 글 수정이 아닌 새롭게 생성되고 있다. 이를 수정하시오.
@require_http_methods(['GET', 'POST'])
def update(request, pk):
    item = Item.objects.get(pk=pk)
    if request.method == 'POST':
        form = ItemForm(request.POST, instance=item) #instance 추가
        if form.is_valid():
            form.save()
            return redirect('shops:detail', pk)

    else:
        form = ItemForm(instance=item) #instance 추가
    
    context = {
        'form': form,
        'pk': pk,
    }
    return render(request, 'shops/update.html', context)


@require_POST
def delete(request, pk):
    item = Item.objects.get(pk=pk)
    item.delete()
    return redirect('shops:index')