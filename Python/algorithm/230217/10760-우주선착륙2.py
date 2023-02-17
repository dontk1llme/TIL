# 우주선착륙2 D2
# 아 착륙지 고르기라고
# 하나하나 돌면서 주변 8방향 중 본인보다 작은 수가 4개 이상인 곳만 카운트

T = int(input())
dt = [(1,1), (-1,-1), (1,-1),(-1,1), (0,1), (1,0), (0,-1), (-1,0)]
for tc in range(1, T+1):
    N,M=map(int,input().split())
    lst = [list(map(int,input().split())) for _ in range(N)]

    cnt = 0
    for i in range(N):
        for j in range(M):
            around=0
            for k in range(len(dt)):
                dx,dy = dt[k]
                nx,ny = i+dx, j+dy
                if nx>=0 and nx<N and ny>=0 and ny<M: #범위 내에 있으면
                    if lst[i][j]>lst[nx][ny]:
                        around+=1
            if around>=4:
                # print(f'여기{lst[i][j], i, j}')
                cnt+=1

    print(f'#{tc} {cnt}')

