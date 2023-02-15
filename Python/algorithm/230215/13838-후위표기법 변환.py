# https://velog.io/@jin0106/Python-%ED%9B%84%EC%9C%84%ED%91%9C%EA%B8%B0%EB%B2%95-%EB%B0%8F-%EA%B3%84%EC%82%B0%EB%B2%95
# 연산자: +, *
# 숫자: 0-9 정수

T = int(input())
for tc in range(1,T+1):
    cal = input()
    stk = [] # 연산자 담을 스택
    lst = [] # 답 저장용
    prior = {'*':2, '+':1} # 우선순위 생각 (큰 수가 먼저)

    for i in range(len(cal)):
        if cal[i].isdigit(): # 정수면 append
            lst.append(cal[i])
        else:
            while stk and prior[cal[i]] <= prior[stk[-1]]: # stk이 있고 현재 우선순위가 스택top보다 낮으거나 같으면 (같으면: ++인 경우 하나는 뽑아줘야되니까
                lst.append(stk.pop()) # 스택 다 뽑아내고
            stk.append(cal[i]) # 자기자신을 스택으로 (이렇게 해야 숫자 뒤에 앞연산자들이 나옴)
    while stk: # 스택에 머 남아있으면 다 더해줘야지 후위연산 완성
        lst.append(stk.pop())

    print(f'#{tc}', end=' ')
    ans = ''.join(lst)
    print(ans)
