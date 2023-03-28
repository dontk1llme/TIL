# boj 2468 안전 영역
# https://velog.io/@phw1996/%EB%B0%B1%EC%A4%80-2468%EB%B2%88-%EC%95%88%EC%A0%84-%EC%98%81%EC%97%AD-%ED%8C%8C%EC%9D%B4%EC%8D%AC
# 재귀 위치만 잘 생각하면.  .

import sys
sys.setrecursionlimit(100000) #안 하면 exceed recursion limit 에러

d = [(-1,0), (0,1), (1,0), (0,-1)]
n = int(input())
lst = []
maxrain = 0
for i in range(n):
    lst.append(list(map(int, input().split())))
    for j in range(n):
        if lst[i][j]>maxrain:
            maxrain = lst[i][j]


def check_safe(x,y, rain): #안전구역 찾기
    for m in range(4):
        nx, ny = x+d[m][0], y+d[m][1]
        if 0<=nx<n and 0<=ny<n and not visited[nx][ny] and lst[nx][ny]>rain:
            visited[nx][ny]=1
            check_safe(nx,ny,rain)

ans = 1
for i in range(maxrain):
    visited = [[0]*n for _ in range(n)]
    cnt = 0

    for j in range(n):
        for k in range(n):
            if lst[j][k] > i and visited[j][k]==0:
                cnt+=1
                visited[j][k] = 1
                check_safe(j,k,i)
    ans = max(ans, cnt)

print(ans)
