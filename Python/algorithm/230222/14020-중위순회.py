#  [S/W 문제해결 기본] 9일차 - 중위순회 (제출용) D4

def inord(n):
    if n:
        inord(left[n])
        print(ch[n], end='')
        inord(right[n])

T = 10
for tc in range(1,T+1):
    N = int(input())
    ch = [[] for _ in range(N+1)]
    left = [[] for _ in range(N+1)]
    right = [[] for _ in range(N+1)]
    for i in range(N):
        lst = list(map(str, input().split()))
        lst[0]=int(lst[0])
        for k in range(len(lst)):
            if k==1: ch[lst[0]]=lst[k]
            elif k==2: left[lst[0]]=int(lst[k])
            elif k==3: right[lst[0]]=int(lst[k])

    # print(ch)
    # print(left)
    # print(right)
    print(f'#{tc} ', end='')
    inord(1)
    print()
