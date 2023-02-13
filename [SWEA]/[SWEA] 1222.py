# 1222. [S/W 문제해결 기본] 6일차 - 계산기1 D4

T =10
for tc in range(1,T+1):
    N = int(input())
    s = input()
    num=[]
    cal=[]
    ans = 0
    for i in range(N):
        if s[i]!='+':
            num.append(int(s[i]))
        else: cal.append(s[i])

    for i in range(len(cal)+1):
        ans += num[i]

    print(f'#{tc} {ans}')
