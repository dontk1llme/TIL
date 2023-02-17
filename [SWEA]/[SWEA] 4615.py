# 4615. 재미있는 오셀로 게임 D3
# A형 기출이래

#크기가 N*N이고 중앙에 돌 4개가 놓여있는 형태로 배열을 초기화한다.
#입력 받은 위치에 돌을 내려놓고 상, 하, 좌, 우, 좌상, 우상, 좌하, 우하 8가지 방향에 다른 색의 돌이 놓여있는지 확인
#돌이 있다면 그 방향으로 계속 검사를 진행하며, 공백이 나타나면 초기화하고 같은 색의 돌이 나오면 여태 나온 돌의 색을 바꿔준다.
# https://velog.io/@jinho0705/SWEA-4615.-%EC%9E%AC%EB%AF%B8%EC%9E%88%EB%8A%94-%EC%98%A4%EC%85%80%EB%A1%9C-%EA%B2%8C%EC%9E%84python
# https://dodonmountain.github.io/p&othe/



T = int(input())
delta = [(1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1)]
for tc in range(1, T+1):
    N,M = map(int,input().split())
    board = [[0]*(N) for _ in range(N)]
    board[N//2][N//2-1], board[N//2-1][N//2] = 1,1 #흑돌자리
    board[N//2-1][N//2-1], board[N//2][N//2] = 2,2 #백돌자리

    play = []
    for _ in range(M):
        y,x,c = map(int, input().split()) #c 1: 흑돌, c 2: 백돌 # x,y 반대라 뒤집어받기
        y-=1
        x-=1 #인덱스

        #배열 놓는 걸 할 줄 모르겠어.... 아래는 다 베낀 것.
        #델타 쓰는 방법 연습
        if not board[x][y]:
            board[x][y]=c
            for i in range(len(delta)):
                dx,dy = delta[i]
                nx,ny = x+dx, y+dy
                #뒤집을 좌표 저장
                reverse = []
                while True:
                    #다음 검사 값이 배열에 있는지 확인
                    if nx<0 or N-1<nx or ny<0 or N-1<ny: #없으면
                        reverse=[]
                        break
                    #공백인지
                    if board[nx][ny]==0:
                        reverse=[]
                        break
                    #같은 색 만나면 멈춤
                    if board[nx][ny] ==c:
                        break
                    #다른 색이면 좌표 저장
                    else:
                        reverse.append((nx,ny))
                    nx+=dx
                    ny+=dy
                #색 뒤집기
                for rx,ry in reverse:
                    board[rx][ry]=c
    w,b = 0,0
    for i in range(N):
        for j in range(N):
            if board[i][j]==1:
                w+=1
            elif board[i][j]==2:
                b+=1
    print(f'#{tc} {w} {b}')
