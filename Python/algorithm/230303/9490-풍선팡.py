# 9490. 풍선팡

di = [-1,1,0,0]
dj = [0,0,-1,1]

T = int(input())
for tc in range(1, T+1):
    N,M = map(int, input().split())
    lst =[list(map(int, input().split())) for _ in range(N)]
    ans = 0

    for i in range(N):
        for j in range(M):
            cnt = K = lst[i][j]
            for d in range(4):
                for k in range(1,K+1):
                    ni, nj = i+di[d]*k, j+dj[d]*k
                    if 0<=ni<N and 0<=nj<M:
                        cnt += lst[ni][nj]
            if cnt > ans : ans = cnt

    print(f'#{tc} {ans}')