# 1217 [S/W 문제해결 기본] 4일차 - 거듭 제곱 (제출용)

T = 10

def power(n,m):
    if m==0:
        return 1
    else: return n*power(n,m-1)

for _ in range(1, T+1):
    tc = int(input())
    N,M = map(int, input().split())
    print(f'#{tc} {power(N,M)}')