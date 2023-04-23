#1432. 데일리과제 1-4. 자릿수 출력 예제

#사용자가 입력한 각 자릿수를 더해 출력하는 코드를 작성하라.
s = input('숫자를 입력해주세요 : ')
i = len(s)
a=0
total = 0
while a<i:
    total = total+int(s[a])
    a+=1
print(total)