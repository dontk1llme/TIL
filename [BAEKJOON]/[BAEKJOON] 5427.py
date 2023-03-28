# boj 5427 불
# 불 위치를 어케 다룰지 . . . https://velog.io/@ckstn0778/%EB%B0%B1%EC%A4%80-5427%EB%B2%88-%EB%B6%88-O-1-Python
# 큐를 만들어서 사람 위치랑 불 위치랑 따로 관리해 줘도 되고, 윗글에서는 하나의 큐로 해버렸음
# 나는 편의상 두개 나눠서 할랩... https://2hs-rti.tistory.com/entry/%EB%B0%B1%EC%A4%80-5427%EB%B2%88-%EB%B6%88-%ED%8C%8C%EC%9D%B4%EC%8D%AC

from collections import deque

T = int(input())

dx, dy = [0,0,-1,1], [1,-1,0,0]

def burn():
    for _ in range(len(fire)):
        x,y = fire.popleft()
        for k in range(4):
            nx,ny = x+dx[k], y+dy[k]
            if 0<=nx<h and 0<=ny<w:
                if lst[nx][ny]!='#' and lst[nx][ny]!='*':
                    lst[nx][ny]='*'
                    fire.append((nx,ny))

def move():
    go = False
    for _ in range(len(start)):
        x,y=start.popleft()
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if 0 <= nx < h and 0 <= ny < w:
                if visited[nx][ny]==0 and lst[nx][ny]!='#' and lst[nx][ny]!='*':
                    go = True
                    visited[nx][ny]=visited[x][y]+1 #이러면 누적돼서 자연스럽게 답이 됨
                    start.append((nx,ny)) #다음 시작점
            else: return visited[x][y]
    if not go:
        return 'IMPOSSIBLE'


for tc in range(1, T+1):
    w,h = map(int,input().split())
    lst = []
    fire = deque()
    start = deque()
    visited = [[0]*w for _ in range(h)]
    for i in range(h):
        lst.append(list(map(str,input())))
        for j in range(w):
            if lst[i][j]=='@':
                start.append((i,j))
                visited[i][j]=1
            elif lst[i][j]=='*':
                fire.append((i,j))

    ans = 0
    while True:
        burn()
        ans = move()
        if ans:
            break

    print(ans)