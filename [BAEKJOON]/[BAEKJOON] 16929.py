# BOJ 16929 Two Dots
# 방향을 다 다르게 3번 바꾸고, 시작점에 다시 돌아오는지 확인하면 되지 않을까
# ㄴㄴ 3번이 아님... 그냥 시작점에 안끊기고 돌아오기만 하면 되네요 같은 문자 최소 4개가 필요할뿐
# 시작점 주의
# https://data-flower.tistory.com/100 함수에 넣을 요소들 체크할때 참고

dx=[-1,1,0,0]
dy=[0,0,-1,1]

n,m = map(int, input().split())
lst = [list(map(str, input())) for _ in range(n)]
visited=[[0]*m for _ in range(n)]
ans = False

#시작점에서부터 사이클 되는지 확인
def check(x,y,cnt,col,starti, startj):
    global ans
    if ans:
        return
    for k in range(4):
        nx,ny = x+dx[k], y+dy[k]
        if 0<=nx<n and 0<=ny<m:
            if cnt>=4 and nx == starti and ny==startj:
                ans=True
                return
            if lst[nx][ny]==col and visited[nx][ny]==0:
                visited[nx][ny]=1
                check(nx,ny,cnt+1,col,starti, startj)
                visited[nx][ny]=0

for i in range(n):
    for j in range(m):
        cnt=1
        starti, startj = i,j
        visited[i][j] = 1  # 시작점만
        check(i,j,cnt,lst[i][j],starti, startj)

        if ans:
            break
    if ans:
        break
if ans: print('Yes')
else: print('No')