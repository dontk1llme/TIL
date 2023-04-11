# boj 3055 탈출

# https://velog.io/@ms269/%EB%B0%B1%EC%A4%80-3055-%ED%83%88%EC%B6%9C-%ED%8C%8C%EC%9D%B4%EC%8D%AC-Python
# https://kyun2da.github.io/2020/09/22/escape/
# https://sinsomi.tistory.com/entry/%EB%B0%B1%EC%A4%80-Python-3055%EB%B2%88-%ED%83%88%EC%B6%9C-%EC%B4%88%EC%BD%94%EB%8D%94
# https://campkim.tistory.com/16

# D -> S. 최단시간 -> BFS
# 고슴도치: 한번에 1칸 이동, .으로만 이동 가능
# 물: 한번에 1칸씩 확장, x/d 면 이동 불가
# 물 채우고 고슴도치 이동하고 시간 +하기
#//////////////////////////////////////////////////////////////////////

from collections import deque

dlst= [(0,1), (1,0), (-1,0), (0,-1)]

R, C = map(int,input().split())
lst = [list(map(str, input())) for _ in range(R)]
x,y = 0,0
queue = deque()
for i in range(R): 
    for j in range(C):
        if lst[i][j]=='D': #도착점
            D = i,j
        elif lst[i][j]=='*': #물 위치 기록 후 큐에
            queue.append([i,j,'*'])
        elif lst[i][j]=='S': #시작점
            lst[i][j]==1
            S = [i,j,0] #0: 고슴도치 루트를 int로 판별하기 위해 + 시간 계산
queue.append(S) #물이 큐에 모두 들어간 후에 고슴도치 넣음

while queue:
    x,y,z = queue.popleft()
    if x==D[0] and y==D[1]: #도착한 경우
        print(z)
        break
    else: 
        for i in range(4):
            nx, ny = x+dlst[i][0], y+dlst[i][1] 
            if (z=='*' and 0<=nx<R and 0<=ny<C and 
                lst[nx][ny]!='X' and lst[nx][ny]!='D' and lst[nx][ny]!='*'): #물 퍼지기
                lst[nx][ny] = '*'
                queue.append([nx,ny,'*'])
            elif (type(z)==int and 0<=nx<R and 0<=ny<C and 
                    (lst[nx][ny]=='.' or lst[nx][ny]=='D')): #고슴도치 움직이기
                lst[nx][ny] = z+1 #시간 계산 그냥 바로 때려버리기
                queue.append([nx,ny,z+1])
    if len(queue)==0: #물 다 퍼졌는데도 목적지에 도달 못하면 이 코드까지 옴
        print('KAKTUS')
        break
                