# 2213. 데일리과제 2-2. 카페 주문 건수 출력하기 예제

orders = '아이스아메리카노,카라멜마키야또,에스프레소,아메리카노,아메리카노,아이스라떼,핫초코,아이스아메리카노,아메리카노,아이스카라멜마키야또,아이스라떼,라떼마키야또,카푸치노,라떼마키야또'
orderlist=[]
orders=orders.split(',')
print(orders)

print(f'총 몇 잔?: {len(orders)}')
for i in orders:
    if i not in orderlist:
        orderlist.append(i)
orderlist.sort()
print(orderlist)
