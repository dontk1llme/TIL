#BOJ 14503 로봇청소기, 삼성기출
# 청소기는 lst 0이면 청소 안됨, 1이면 벽임. 청소햇으면 2로 바꿀거임
# 다 청소: 한칸 후진. 벽이면 작동멈춤 (다청소여부: flag 만들기)
# 청소 안함: 왼쪽으로 회전(d: 0,3,2,1 순서), 앞칸 빈칸이면 한칸 전진
# 조건 참고 https://resilient-923.tistory.com/164


# d 0:북, 1:동, 2:남, 3:서
dlst = [(-1,0),(0,1), (1,0), (0,-1)]

N,M = map(int, input().split())
r,c,d = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(N)]
visited=[[0]*M for _ in range(N)] #방문

visited[r][c]=1 #처음 방문하는 곳
ans=1 #청소한 개수(처음 잇는 곳은 무조건이라 1부터)

while 1:
    flag=0
    for _ in range(4):
        nx = r + dlst[(d+3)%4][0] #반시계 방향 맞추려고
        ny = c + dlst[(d+3)%4][1]
        d = (d+3)%4
        if 0<=nx<N and 0<=ny<M and lst[nx][ny]==0:
            if visited[nx][ny]==0:
                visited[nx][ny]=1
                ans+=1
                r, c = nx, ny
                #청소햇으면 그냥 넘어감!
                flag=1
                break

    if flag==0: #4방향 모두 청소되어 있음
        if lst[r-dlst[d][0]][c-dlst[d][1]]==1: #후진햇는데 벽
            print(ans)
            break
        else:
            r,c = r-dlst[d][0], c-dlst[d][1]
