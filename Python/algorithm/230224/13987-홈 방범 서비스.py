# 2117. [모의 SW 역량테스트] 홈 방범 서비스
# 운영비용 = 서비스영역의 면적 (맵 넘어가도 그냥 그대로) =  K * K + (K - 1) * (K - 1)
# 진짜 모르겟는데 bfs래.. 힝
# 교수님 설명듣자...
# https://chelseashin.tistory.com/62
# https://week-year.tistory.com/143

dx = [-1,1,0,0]
dy = [0,0,1,-1]
Klst = [k*k+(k-1)*(k-1) for k in range(26)] #k의 값 리스트. 왜 26일까?

def bfs(sr, sc):
    global cnt
    visited = [[0]*N for _ in range(N)]
    visited[sr][sc]=1
    q = list([(sr,sc)])

    home = lst[sr][sc]
    dis = 1
    # 1 크기일 때도 검사
    if home * M - Klst[dis] >=0:
        cnt = max(home, cnt)
    while dis<N+2:
        qlen = len(q)
        for _ in range(qlen):
            r,c = q.pop(0)
            for k in range(4):
                nr, nc = r+dx[k], c+dy[k]
                if 0<=nr<N and 0<=nc<N:
                    if not visited[nr][nc]:
                        visited[nr][nc]=1
                        q.append([nr,nc])
                        if lst[nr][nc]:
                            home+=1
        if home*M-Klst[dis+1]>=0:
            cnt = max(home, cnt)
        dis+=1

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    lst = [list(map(int ,input().split())) for _ in range(N)]
    cnt=0
    for i in range(N):
        for j in range(N):
            bfs(i,j)
    print(f'#{tc} {cnt}')

#/////////////////
#4중FOR문

from collections import deque

dr = (-1, 1, 0, 0)
dc = (0, 0, -1, 1)
KLst = [k*k+(k-1)*(k-1) for k in range(26)]     # K의 값 리스트 미리 구해놓기

# main
T = int(input())
for tc in range(T):
    N, M = map(int, input().split())
    A = []
    homeLst = []
    for i in range(N):
        A.append(list(map(int, input().split())))
        for j in range(N):
            if A[i][j]:
                homeLst.append((i, j))
    # print(homeLst)
    maxCnt = 0
    for k in range(1, N+2):
        for i in range(N):
            for j in range(N):
                home = 0
                for r, c in homeLst:
                    if abs(i-r) + abs(j-c) < k:
                        home += 1
                if home * M - KLst[k] >= 0:
                    maxCnt = max(home, maxCnt)

    print("#{} {}".format(tc+1, maxCnt))