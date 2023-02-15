#  [파이썬 S/W 문제해결 기본] 5일차 - 미로 (제출용) D2
# 0:길, 1:벽, 2:출발, 3:도착

dx = [-1,1,0,0]
dy = [0,0,-1,1]

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    miro = [list(input()) for _ in range(N)]

    #출발지 찾기 (2)
    x,y=0,0
    for i in range(N):
        for j in range(N):
            if miro[i][j]=='2':
                x,y=i,j

    #DFS
    stk = [(x,y)]
    reach = 0
    while stk:
        cx,cy = stk.pop()
        for k in range(4):
            nx = cx + dx[k]
            ny = cy + dy[k]
            if 0<=nx<N and 0<=ny<N:
                if miro[nx][ny]=='0':
                    stk.append((nx,ny))
                    miro[nx][ny]=9 #다신안옴
                #목적지 도달하면
                elif miro[nx][ny] == '3':
                    reach = 1
                    stk.clear() #while문 나가기
                    break  #for문 나가기

    print(f'#{tc} {reach}')