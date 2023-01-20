# 1690. 데일리실습 4-4. ord 함수를 이용한 숫자 구하기 예제
word1 = input('첫 번째 이름을 입력하세요 : ')
word2  = input('두 번째 이름을 입력하세요 : ')


def get_strong_word(a,b):
    num1, num2=0,0
    for i in range(0,len(a)):
        num1+=ord(a[i])
    for j in range(0,len(b)):
        num2+=ord(b[j])
    if num1>num2: return a
    elif num2>num1: return b
    else: return 'same'

print(get_strong_word(word1,word2))