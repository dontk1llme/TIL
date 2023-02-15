# 1223. [S/W 문제해결 기본] 6일차 - 계산기2 D4

T = 10
for tc in range(1,T+1):
    l = int(input())
    cal = input()
    stk = [] #연산자
    lst = [] #출력
    prior={'*':2, '+':1}

    #후위계산식 만들기
    for i in range(len(cal)):
        if cal[i].isdigit():
            lst.append(cal[i])
        else:
            while stk and prior[cal[i]]<=prior[stk[-1]]:
                lst.append(stk.pop())
            stk.append(cal[i])
    while stk: #위치 조심
        lst.append(stk.pop())
    # print(lst)

    #만든 식 토대로 계산하기
    ans=0
    num = []
    for i in range(len(lst)):
        if lst[i].isdigit():
            num.append(int(lst[i]))
        else:
            if len(num)>=2:
                num2 = num.pop()
                num1 = num.pop()
                if lst[i]=='*':
                    num.append(num1*num2)
                elif lst[i]=='+':
                    num.append(num1+num2)
            # else:
            #     if lst[i]=='*':
            #         ans=num.pop()*int(lst[i-1])
            #     elif lst[i]=='+':
            #         ans=num.pop()+int(lst[i-1])
    print(f'#{tc} {num[0]}')
