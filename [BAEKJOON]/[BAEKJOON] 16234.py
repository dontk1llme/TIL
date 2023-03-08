# boj 16234 인구이동
# 우와 어캐하지? => BFS
# bfs와 큐를 적당히 활용하는 연습.. 해야 할 거 같아요
# 사실 봐도 잘 모르겟다! 좀 더 생각해 보기
# https://developer-ellen.tistory.com/40

from collections import deque

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(a,b):
    connect = deque()
    people, count = 0,0 #연합 저장용
    visited[a][b] =1
    while q:
        x,y = q.popleft()
        connect.append((x,y))
        count+=1
        people+=lst[x][y]
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if 0<=nx<N and 0<=ny<N:
                if visited[nx][ny]==0:
                    diff = abs(lst[x][y]-lst[nx][ny])
                    if L<=diff<=R: #국경선 공유하기 위해서 방문처리, 공유한 위치를 q에 append
                        visited[nx][ny]=count
                        q.append((nx,ny))

    while connect:
        x,y = connect.popleft()
        lst[x][y]=(people//count)
    if count==1:
        return 0
    return 1

N,L,R = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(N)]
ans = 0
while True:
    q = deque()
    break_cnt=0
    visited = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if visited[i][j] ==0:
                q.append((i,j))
                break_cnt+=bfs(i,j)
    if break_cnt==0: #국경선을 공유하지 않았을 경우
        break
    else: #국경선을 공유한 국가가 있다면...
        ans+=1
print(ans)

