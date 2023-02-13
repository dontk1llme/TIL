# 13801 [S/W 문제해결 기본] 10일차 - 비밀번호 (제출용)
# same with 4873

T = 10
for tc in range(1, T+1):
    n, s = map(str, input().split())
    n = int(n)
    stk=[]
    for i in range(n):
        if len(stk)==0:
            stk.append(s[i])
        elif s[i]==stk[-1]:
            stk.pop()
        else: stk.append(s[i])

    print(f'#{tc}', end=' ')
    result = ''.join(stk)
    print(result)


