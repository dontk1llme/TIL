# boj 1937 욕심쟁이 판다
# 원래 있던 지점보다 적으면 안 감
# 최대한 많은 칸 방문해야 함
# dp, dfs 같이 사용해야 함! https://kyun2da.github.io/2021/04/04/panda/
# https://my-coding-notes.tistory.com/315

import sys
sys.setrecursionlimit(10 ** 6)

def dfs(x,y):
    if dp[x][y]: return dp[x][y] #한번 왔다간 경로는 그대로 리턴
    dp[x][y] = 1
    for i in range(4):
        nx, ny = x+d[i][0], y+d[i][1]
        if 0<=nx<N and 0<=ny<N and lst[x][y]<lst[nx][ny]:
            dp[x][y] = max(dp[x][y], dfs(nx,ny)+1) #+1은 머임?
    return dp[x][y]

d = [(0,1),(1,0),(0,-1),(-1,0)]
N = int(input())
lst = [list(map(int, input().split())) for _ in range(N)]
dp = [[0]*N for _ in range(N)]

ans = 0
for i in range(N):
    for j in range(N):
        ans = max(ans, dfs(i,j))

print(ans)