#  [파이썬 S/W 문제해결 기본] 6일차 - 미로의 거리 (제출용) D3

dx = [0, 0, 1, -1]
dy = [-1, 1, 0, 0]
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    lst = [list(map(int, input())) for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if lst[i][j] == 3: #걍 3에서 2로 가는거라고 생각함
                r,c=i,j
                break
    q = []
    visited = [[0]*N for _ in range(N)]
    q.append((r,c))
    visited[r][c]=1
    possible = 0 #일단 불가능하다고...
    while q:
        r,c = q.pop(0)
        if lst[r][c]==2: #답에 도달햇으니까
            possible=visited[r][c] -2 #출발,도착 빼고
            break
        for i in range(4):
            nr, nc = r+dx[i], c+dy[i]
            if 0<=nr<N and 0<=nc<N and not visited[nr][nc]: #범위 내이고 방문하지 않앗으면
                if lst[nr][nc]!=1:#벽 아니면
                    visited[nr][nc]=visited[r][c]+1 #몇번째인지...
                    q.append((nr,nc))
    # print(visited)

    print(f'#{tc} {possible}')






