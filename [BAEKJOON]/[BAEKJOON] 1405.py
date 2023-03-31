# boj 1405 미친로봇
# 배열 만들어주고 방문 확인하면서 하면 될듯
# 확률 찾는걸 모름...0.01
# https://summa-cum-laude.tistory.com/36

dx,dy = [0,0,1,-1],[1,-1,0,0] #동서남북 맞춰줌
def dfs(x,y,cnt,p):
    global ans

    if cnt==times:
        ans+=p
        return
    for i in range(4):
        nx,ny = x+dx[i], y+dy[i]
        if lst[nx][ny]:
            continue
        if not 0<=nx<(2*times)+1 or not 0<=ny<(2*times)+1:
            continue
        lst[nx][ny]=1
        dfs(nx,ny,cnt+1, p*poss[i]*0.01 )
        lst[nx][ny]=0

times, E, W, S, N = map(int, input().split())
poss = [E,W,S,N]
lst = [[0]*(2*times+1) for _ in range(2*times+1)] #한 방향으로 최대 n번 가니까 행렬 크기
lst[times][times]=1
ans = 0
dfs(times,times,0,1)
print(ans)
