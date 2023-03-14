# boj 2573 빙산
# visit 써줘야지만 수월한 순회 가능함
# 그냥 deepcopy 하니까 시간초과남
# 그래서 여기 참고함 https://77dptjd.tistory.com/9
# sys 안 쓰거나 limit 안 걸어줘도 런타임 에러 남 ;; 참나
# 31에서 시간초과 무슨 일이고... -> pypy로 하니까 됨. ;;

import sys
sys.setrecursionlimit(10**5)

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def dfs(i,j):
    for k in range(4):
        nx = i+dx[k]
        ny = j+dy[k]
        if 0<=nx<N and 0<=ny<M and visit[nx][ny]:
            visit[nx][ny]=False #방문초기화
            if lst[nx][ny]!=0:
                dfs(nx,ny)

input = sys.stdin.readline
N,M = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(N)]
visit=[[False]*M for _ in range(N)] #방문 체크
year = 0

while True:
    # 빙산 줄이기
    year += 1
    for i in range(N):
        for j in range(M):
            if lst[i][j]!=0:
                visit[i][j]=True #원래 상태에서 빙하를 재야 하니까 visit 사용
                tmp = lst[i][j]
                for k in range(4):
                    nx = i+dx[k]
                    ny = j+dy[k]
                    if 0<=nx<N and 0<=ny<M and not visit[nx][ny]: #visit까지 봐줘야함
                        if lst[nx][ny]==0:
                            tmp-=1
                            if tmp==0: #0이 되면 멈춤
                                break
                lst[i][j]=tmp #녹은 빙하 저장


    # 몇 덩이인지 확인하기 (1덩이가 아니면 year 출력)
    cnt = 0 #빙하 개수
    for i in range(N):
        for j in range(M):
            if lst[i][j]!=0 and visit[i][j]: #빙하 있으면 dfs 해서 계속 확인함
                dfs(i,j)
                cnt+=1
            elif lst[i][j]==0 and visit[i][j]: #이제 빙하 없으면 방문초기화! (재사용 해야함)
                visit[i][j] = False

    if cnt!=1: # 2 이상이면 2 이상인 개수 출력, 0이면 한번에 다 녹았다는 거니가 그냥 1이 아닌 경우만 뽑아주면 됨
        if cnt==0:
            print(0)
        else: print(year)
        break