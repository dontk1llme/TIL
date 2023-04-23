#1681. 데일리실습 3-2. 조건문을 이용한 문자열 슬라이

str = input()

l = len(str)%2
p = len(str)//2

if l!=0:
    print(str[p])
elif l==0: 
    print(str[p-1]+str[p])
