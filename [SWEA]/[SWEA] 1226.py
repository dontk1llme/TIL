# 1226. [S/W 문제해결 기본] 7일차 - 미로1 D4
# 그냥 상하좌우 다 탐색. 길 만나면 스택에 추가, 그리고 다시 안 가기 위해서 값 9로 바꿔줌
# 3 만나면 끝이니까 종료 (걍 가능하기만 하면 됨)

#DFS/////////////////////////////////////
xlst = [-1, 1, 0, 0]  # 위, 아래
ylst = [0, 0, -1, 1]  # 좌,우

T = 10
for _ in range(1,T+1):
    tc = int(input())
    miro = [list(map(int, input())) for _ in range(16)]
    reach=0 #도달하면 1, 아니면 0
    x,y=0,0 #시작점
    #시작점 찾기
    for i in range(16):
        for j in range(16):
            if miro[i][j]==2:
                x,y=i,j

    #미로 DFS
    stk = [(x,y)]
    while stk:
        cx, cy = stk.pop()
        for k in range(4):
            nx = cx + xlst[k]
            ny = cy + ylst[k]
            if 0<= nx < 16 and 0<= ny < 16:
                #길 추가
                if miro[nx][ny]==0:
                    stk.append((nx, ny))
                    miro[nx][ny]=9 #다시 안 오기 위해...
                #끝
                elif miro[nx][ny]==3:
                    reach = 1
                    stk.clear()
                    break

    print(f'#{tc} {reach}')

    
#///////////////////////////////////////////////////
#BFS

dx = [0,0,-1,1]
dy = [1,-1,0,0]
for _ in range(10):
    tc = int(input())
    lst = [list(map(int, input())) for _ in range(16)]
    for i in range(16):
        for j in range(16):
            if lst[i][j]==2: #출발점
                r,c = i,j
                break

    visited = [[0] * 16 for _ in range(16)]
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
            if 0<=nr<16 and 0<=nc<16 and not visited[nr][nc]:
                if lst[nr][nc]!=1:
                    visited[nr][nc] =  1 #들럿셔
                    q.append((nr, nc))

    print(f'#{tc} {ans}')
