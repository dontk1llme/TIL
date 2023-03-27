#  [파이썬 S/W 문제해결 구현] 2일차 - 최소합 (제출용) D3
# https://independenceday.tistory.com/entry/SWEA-5188-%EC%B5%9C%EC%86%8C%ED%95%A9-python


d = [(0,1), (1,0)] #오른쪽이나 아래로만 이동가능
T = int(input())
def road(x,y,total):
    global ans
    if x==N-1 and y==N-1: #도착하면
        total+=lst[x][y]
        if total<ans:
            ans=total
        return
    if total>ans: #더하는게 현재 최소값보다 커지면 계산할 필요가 없음
        return

    for i in range(2):
        nx, ny = x+d[i][0], y+d[i][1]
        if 0<=x<N and 0<=y<N and not visited[x][y]:
            visited[x][y]=1
            road(nx, ny, total+lst[x][y])
            visited[x][y]=0


for tc in range(1, T+1):
    N = int(input())
    lst = [list(map(int, input().split())) for _ in range(N)]
    ans = N*10*2 #나올 수 있는 최대값
    visited = [[0]*N for _ in range(N)]

    road(0,0,0)
    print(f'#{tc} {ans}')