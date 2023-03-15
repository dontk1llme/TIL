from django.shortcuts import render

# Create your views here.
def price(request, product, won):

    product_price = {"라면":980,"홈런볼":1500,"칙촉":2300, "식빵":1800}

    if product in product_price:
        context = {
            'thing' :product,
            'cnt':won,
            'total': won * product_price[product],
            'flag':True #잇냐 없냐 구분하기 위해 넣음
        }
    else:
        context = {
            'thing' :product,
            'flag':False
        }

    return render(request, 'prices/price.html', context)

    # context = {
    #     'product_price' : {"라면":980,"홈런볼":1500,"칙촉":2300, "식빵":1800},
    #     'product' : product,
    #     'won' : won,
    # }
    # return render(request, 'prices/price.html', context)
    # 이렇게 하는 방법도 잇다~는뜻
