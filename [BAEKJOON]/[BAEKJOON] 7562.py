# 7562. 나이트의 이동
# bfs!
from collections import deque

d = [(1,2), (-1,2),(1,-2), (-1,-2), (2,1), (2,-1), (-2,1), (-2,-1)] #8방향

def bfs(r,c,nr,nc):
    q = deque()
    q.append((r,c))

    while q:
        x,y = q.popleft()
        if x==nr and y==nc:
            print(visited[x][y]-1)
            return True
        for i in range(8):
            nx,ny = x+d[i][0], y+d[i][1]
            if nx < 0 or nx >= l or ny < 0 or ny >= l:
                continue
            if visited[nx][ny] ==0:
                visited[nx][ny]=visited[x][y]+1
                q.append((nx,ny))
    return False

T = int(input())
for tc in range(1, T+1):
    l = int(input()) #체스판의 한 변의 길이
    visited = [[0]*l for _ in range(l)]

    r,c= map(int, input().split()) #현재 위치
    nr,nc = map(int,input().split()) #가야 할 곳
    visited[r][c] = 1
    bfs(r,c,nr,nc)


