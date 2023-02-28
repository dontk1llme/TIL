#  Start_연습문제_2_십육진수의 십진수 출력 (제출용) D2

T = int(input())
for tc in range(1, T+1):
    lst = input()

    #16->2진수
    bitlst = []
    for x in lst:
        n = int(x,16)
        for j in range(3,-1,-1):
            bit = 1 if n&(1<<j) else 0
            bitlst.append(bit)

    #7개씩 끊어서 10진수
    num = 0
    last = len(bitlst)%7 #비트가 7로 나누어떨어지지 않아서...
    print(f'#{tc}', end=' ')
    for i in range(len(bitlst)-last):
        j = i % 7  # 2의 n승
        num += bitlst[i] * (2 ** (6 - j))  # 자릿수 더하기
        if j == 6:  # 7개 끊기
            print(num, end=' ')  # 출력하고 num 초기화
            num = 0
    for i in range(1,last+1): #범위 주의...
        # print(bitlst[-i] * (2 ** (i-1)))
        num += bitlst[-i] * (2 ** (i-1))
    print(num)