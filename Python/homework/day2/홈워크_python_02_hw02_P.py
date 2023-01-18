# 2214. 데일리과제 2-4. 카페 메뉴 주문 받기 예제

orders = '아이스아메리카노,카라멜마키야또,에스프레소,아메리카노,아메리카노,아이스라떼,핫초코,아이스아메리카노,아메리카노,아이스카라멜마키야또,아이스라떼,라떼마키야또,카푸치노,라떼마키야또'
orders=list(orders.split(','))
print(orders)
ice=0

#1. 아이스 음료 주문이 몇 개 들어왔는지 확인하세요.
for i in orders:
    if '아이스' in i:
        ice+=1
print('아이스 음료 주문은 ' + str(ice)+' 잔')

#2. 메뉴 별 주문 수를 출력하세요.
neworders=set(orders) #set으로 바꾸면 자동으로 중복제거
neworders=list(neworders)
for i in range(len(neworders)):
    cnt = orders.count(neworders[i])
    print(f'{neworders[i]}의 주문 수는 {cnt}잔')