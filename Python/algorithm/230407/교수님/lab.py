from itertools import combinations
from copy import deepcopy
from collections import deque

n, m = map(int,input().split())

lst = [list(map(int,input().split())) for _ in range(n)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

candidates = []
virus = []
wall = 0

for i in range(n):
    for j in range(m):
        if lst[i][j] == 0:
            candidates.append((i,j))
        elif lst[i][j] == 2:
            virus.append((i,j))
        elif lst[i][j] == 1:
            wall += 1

tmp_walls = list(combinations(candidates, 3))
answer = m*n

for tmp_wall in tmp_walls:
    infested_virus = 0
    flag = 0
    grid = deepcopy(lst)
    for i,j in tmp_wall:
        grid[i][j] = 1

    now_virus = deque(virus)

    while now_virus:
        x, y = now_virus.popleft()

        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if 0<=nx<n and 0<=ny<m:
                if grid[nx][ny] == 0:
                    grid[nx][ny] = 2
                    infested_virus += 1
                    if answer <= infested_virus:
                        flag = 1
                        break
                    now_virus.append((nx, ny))
        if flag:
            break

    answer = min(answer, infested_virus)



    # 바이러스 확산

print(n*m - len(virus) - wall - answer - 3)