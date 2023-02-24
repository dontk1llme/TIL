# 1227 [S/W 문제해결 기본] 7일차 - 미로2 (제출용) D4

dx = [0,0,-1,1]
dy = [1,-1,0,0]

for _ in range(10):
    tc = int(input())
    lst = [list(map(int, input())) for _ in range(100)]
    for i in range(100):
        for j in range(100):
            if lst[i][j]==2: #출발점
                r,c = i,j
                break

    visited = [[0] * 100 for _ in range(100)]
    visited[r][c]=1
    q = [(r, c)]
    ans=0

    while q:
        r,c = q.pop(0)
        if lst[r][c] == 3: #정답도달
            ans = 1
            break
        for k in range(4):
            nr, nc = r + dx[k], c+dy[k]
            if 1<=nr<100 and 1<=nc<100 and not visited[nr][nc]:
                if lst[nr][nc]!=1:
                    visited[nr][nc] =  1 #들럿셔
                    q.append((nr, nc))

    print(f'#{tc} {ans}')


