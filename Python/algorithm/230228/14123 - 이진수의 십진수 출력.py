# Start_연습문제_1_이진수의 십진수 출력 (제출용) D2
# 교수님 라이브대로

T = int(input())
for tc in range(1, T+1):

    lst = list(map(int, input()))
    N = len(lst)
    num = 0

    print(f'#{tc}', end=' ')
    for i in range(N):
        j = i%7 #2의 n승
        num += lst[i]*(2**(6-j)) #자릿수 더하기
        if j==6: #7개 끊기
            print(num, end=' ') #출력하고 num 초기화
            num = 0
    print()
