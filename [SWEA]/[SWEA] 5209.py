# 5209 [파이썬 S/W 문제해결 구현] 5일차 - 최소 생산 비용 (제출용) D3
# 전기버스 2와 비슷한 유형
# https://mungto.tistory.com/220

def dfs(idx, ssum):
    global ans
    if ssum>=ans:
        return
    if idx==N:
        ans=ssum
    for i in range(N):
        if not v[i]:
            v[i]=1
            dfs(idx+1, ssum+lst[idx][i])
            v[i]=0

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    lst = [list(map(int, input().split()))for _ in range(N)]
    v = [0]*N
    ans = 99*N #최대값
    dfs(0,0)
    print(f'#{tc} {ans}')