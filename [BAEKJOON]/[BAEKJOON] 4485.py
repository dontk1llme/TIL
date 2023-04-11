# boj 4485 녹색 옷 입은 애가 젤다지?
# 젤 오른쪽 아래 칸까지 가면서 잃는 금액 최소!
# 다익스트라 문제인데 난 암생각 없이 BFS로 함...
# BFS https://kangfru.tistory.com/10
# 다익 참고 https://bbbyung2.tistory.com/60

from collections import deque

d = [(0,1), (1,0), (-1,0), (0,-1)]

def bfs(i,j,lst,costs):
    queue = deque()
    queue.append((i,j))
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx, ny = x+d[i][0], y+d[i][1]
            if 0<=nx<N and 0<=ny<N:
                if costs[nx][ny] > costs[x][y]+lst[nx][ny]:
                    costs[nx][ny] = costs[x][y]+lst[nx][ny]
                    queue.append((nx,ny))

tc = 0
while True:
    tc+=1 
    N = int(input())
    if N == 0: break
    lst = [list(map(int, input().split())) for _ in range(N)]
    costs = [[int(1e9)]*N for _ in range(N)] #비용그래프
    costs[0][0] = lst[0][0]
    bfs(0,0,lst,costs)
    ans = costs[N-1][N-1]
    print(f'Problem {tc}: {ans}')