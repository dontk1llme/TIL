# boj 14502 연구소
# 0은 빈칸, 1은 벽, 2는 바이러스 위치
# 벽 3개 세울 수 있음!
# 0을 랜덤으로 3개 골라서 세운 뒤 바이러스 퍼뜨린 담에 0의 개수가 가장 많은 경우의 개수를 출력
# 아마 백트래킹(벽), 모든 경우의 수->BFS
import copy

d = [[0,1], [1,0], [-1,0], [0,-1]]

def bfs():
    global ans
    tmp_lst = copy.deepcopy(lst)
    # 바이러스 큐 만들기
    virus = []
    for i in range(N):
        for j in range(M):
            if lst[i][j] == 2:
                virus.append((i, j))
    while virus:
        x,y = virus.pop()
        for i in range(4):
            nx, ny = x+d[i][0], y+d[i][1]
            if 0<=nx<N and 0<=ny<M and tmp_lst[nx][ny]==0:
                tmp_lst[nx][ny]=2
                virus.append((nx,ny))
    cnt = 0
    for i in range(N):
        cnt+=tmp_lst[i].count(0)
    ans = max(cnt, ans)

def wall(cnt):  #백트래킹 하며 모든 경우의 수
    if cnt==3:
        bfs()
        return

    for i in range(N):
        for j in range(M):
            if lst[i][j]==0:
                lst[i][j]=1
                wall(cnt+1)
                lst[i][j]=0

N,M = map(int,input().split())
lst = [list(map(int, input().split())) for _ in range(N)]

# #바이러스 큐 만들기
# virus = []
# for i in range(N):
#     for j in range(M):
#         if lst[i][j]==2:
#             virus.append((i,j))

ans = 0
wall(0)
print(ans)
