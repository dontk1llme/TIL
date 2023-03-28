# boj 2638 치즈
# https://resilient-923.tistory.com/318

from collections import deque

dx, dy = [0,0,1,-1], [1,-1,0,0]
N, M = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(N)]

def bfs():
    q = deque()
    q.append([0,0]) #치즈가 있는 경우에는 bfs가 진행되면 안되니까 치즈가 없는 경우 bfs를 진행해주는 식
    visited[0][0]=1
    while q:
        x,y = q.popleft()
        for k in range(4):
            nx, ny = x+dx[k], y+dy[k]
            if 0<=nx<N and 0<=ny<M and visited[nx][ny]==0:
                if lst[nx][ny]>=1: #치즈이면 1씩 더함
                    lst[nx][ny]+=1
                else:
                    visited[nx][ny]=1 #초기화해줄 필요 없음 아래 while에서 돌떄마다 초기화해주는데
                    q.append([nx,ny])
time = 0
while 1:
    visited = [[0]*M for _ in range(N)]
    bfs()
    flag = 0
    for i in range(N):
        for j in range(M):
            if lst[i][j]>=3: #1에서 2변 이상 더해진 거니까 녹아버리거라...
                lst[i][j]=0
                flag=1
            elif lst[i][j]==2:
                lst[i][j]=1
    if flag==1:
        time+=1
    else: #flag 0이면 녹아야할 치즈가 하나도 없다는 뜻
        break

print(time)




