# pgm 67259 경주로 건설
# BFS까지는 알겠는데 DP까지는 생각 안함
# visited에 비용을 저장해서 . . . -> 이러면 두 경우만 비교 가능하면 나머지는 꼬임
# -> 큐에 담아라! https://heyksw.tistory.com/m/6

# board = [[0,0,0,0,0,0,0,1],[0,0,0,0,0,0,0,0],[0,0,0,0,0,1,0,0],[0,0,0,0,1,0,0,0],[0,0,0,1,0,0,0,1],[0,0,1,0,0,0,1,0],[0,1,0,0,0,1,0,0],[1,0,0,0,0,0,0,0]]
# res = 3800
from collections import deque


def solution(board):
    N = len(board)
    directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]  # 상좌하우

    def bfs(x, y, cost, d):
        graph = [[0] * N for _ in range(N)]
        for a in range(N):
            for b in range(N):
                if board[a][b] == 1: graph[a][b] = -1  # 벽을 -1로 설정
        q = deque()
        q.append((x, y, cost, d))
        while q:
            x, y, cost, idx = q.popleft()
            for i in range(len(directions)):
                nx = x + directions[i][0]
                ny = y + directions[i][1]

                if nx < 0 or nx >= N or ny < 0 or ny >= N: continue
                if graph[nx][ny] == -1: continue

                if idx == i:
                    newcost = cost + 100 #직각
                else:
                    newcost = cost + 600 #코너

                if graph[nx][ny] == 0 or ((graph[nx][ny] != 0) and graph[nx][ny] > newcost):
                    q.append((nx, ny, newcost, i))
                    graph[nx][ny] = newcost

                else:
                    continue

        return graph[N - 1][N - 1]

    return min(bfs(0, 0, 0, 2), bfs(0, 0, 0, 3)) #시작점 0,0에서 좌, 상은 안가니까