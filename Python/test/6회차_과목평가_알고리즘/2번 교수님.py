# 싸피로봇
# 전자카트랑 걍 똑같대... 빡통아

T = int(input())

def dfs(n,sm,cur):
    global ans

    if ans<=sm: #가지치기
        return

    if n==N: #정답조건
        if v[A]<v[B]: #A를 먼저 가야함
            ans = min(ans, sm+lst[cur][0]) #복귀비용 더해줌
        return

    for j in range(1,N):
        if v[j]==0:
            v[j]=n
            dfs(n+1, sm+lst[cur][j], j)
            v[j]=0


for tc in range(1, T+1):
    N =int(input())
    lst = [list(map(int, input().split())) for _ in range(N)]
    A,B = map(int,input().split())

    ans = 100*N
    v = [0]*N
    dfs(1,0,0) #방문횟수, 비용, current위치

    print(f'#{tc} {ans}')