#  [파이썬 S/W 문제해결 기본] 6일차 - 회전 (제출용) D2

T = int(input())
for tc in range(1, T+1):
    N,M = map(int, input().split())
    q = list(map(int, input().split()))
    for i in range(M):
        tmp = q[0]
        q=q[1:]
        q.append(tmp)
    print(f'#{tc} {q[0]}')