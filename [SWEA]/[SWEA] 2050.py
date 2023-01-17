#swea 2050. 알파벳을 숫자로 변환 D1

#아스키 코드값으로 변환: ord()
str = input()
for i in str:
    print(ord(i)-64, end=' ')