# 1224. [S/W 문제해결 기본] 6일차 - 계산기3 D4

T = 10
for tc in range(1,T+1):
    num = int(input())
    cal = input()
    stk = []  # 연산자 담을 스택
    lst = []  # 답 저장용
    prior = {'*': 2, '/':2, '-':1, '+': 1, '(':0}  # 우선순위 생각 (큰 수가 먼저)

    for i in range(len(cal)):
        if cal[i].isdigit():  # 알파벳이면 append
            lst.append(cal[i])
        elif cal[i]=='(':
            stk.append(cal[i])
        elif cal[i]==')':
            while stk[-1]!='(':
                lst.append(stk.pop())
            stk.pop()
        else:
            while stk and prior[cal[i]] <= prior[stk[-1]]:  # stk이 있고 현재 우선순위가 스택top보다 낮으거나 같으면 (같으면: ++인 경우 하나는 뽑아줘야되니까
                lst.append(stk.pop())  # 스택 다 뽑아내고
            stk.append(cal[i])  # 자기자신을 스택으로 (이렇게 해야 숫자 뒤에 앞연산자들이 나옴)
    while stk:  # 스택에 머 남아있으면 다 더해줘야지 후위연산 완성
        lst.append(stk.pop())

    ans = 0
    num = []
    for i in range(len(lst)):
        if lst[i].isdigit():
            num.append(int(lst[i]))
        else:
            if len(num) >= 2:  # 이 조건 없어도됨. 다 맞는 식이라서
                num2 = num.pop()
                num1 = num.pop()
                if lst[i] == '*':
                    num.append(num1 * num2)
                elif lst[i] == '+':
                    num.append(num1 + num2)

    print(f'#{tc} {num[0]}')