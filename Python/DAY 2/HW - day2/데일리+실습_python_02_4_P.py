# 1676. 데일리실습 2-4. string interpolation을 활용한 문
# 출력 결과 예시
# 스테이크   50,000
# + VAT     7,500
# 총계 ₩    57,500

steak = int(input())
vat = int(steak*0.15)
sum=steak+vat

#thousands에 , 넣는 법: f'{x:,}'
print(f'스테이크    {steak:,}') 
print(f'+ VAT    {vat:,}')
print(f'총계 ₩    {sum:,}')
