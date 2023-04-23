# 싸피로봇
# 모르겠음

T = int(input())

def dfs(n,ssum):
    global ans
    if ssum>ans: #가지치기
        return
    if n==N: #도착
        ans = min(ssum, ans)

    for i in range(n,N):
        for j in range(N):
            visited[i] = 1
            # if j==b:
            #     if visited[a]!=1:
            #         visited[n] = 0
            #         continue
            dfs(n+1, ssum+lst[i][j])
            visited[i]=0

for tc in range(1, T+1):
    N = int(input())
    lst = [list(map(int, input().split())) for _ in range(N)]
    a,b = map(int, input().split())
    visited=[0]*N

    ans = 100*N*N
    dfs(0,0)
    print(f'#{tc} {ans}')