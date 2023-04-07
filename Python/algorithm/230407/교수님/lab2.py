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

num = 5
# num 은 0, 1, 2 의 범위에 포함되지 않는, 3 이상의 숫자
for idx in range(num, num + len(tmp_walls)):
    tmp_wall = tmp_walls[num-idx]
    infested_virus = 0
    flag = 0
    for i,j in tmp_wall:
        lst[i][j] = idx

    now_virus = deque(virus)

    while now_virus:
        x, y = now_virus.popleft()

        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if 0<=nx<n and 0<=ny<m:
                if lst[nx][ny] != 1 and lst[nx][ny] != 2 and lst[nx][ny] != idx:
                    lst[nx][ny] = idx
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