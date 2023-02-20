# 탐사로봇

T = int(input())
d = [(0,1), (1,0), (0,-1), (-1,0)]
for tc in range(1, T+1):
    N = int(input())
    lst = [list(map(int, input().split())) for _ in range(N)]
    ans = []

    x,y=0,0
    while True:
        k = lst[x][y]
        if k < 5: #k가 4 미만이어야 해당
            ans.append(k)
            nx, ny = x+d[k][0], y+d[k][1] #이동할 목적지의 인덱스
        else: break
        if 0<=nx<N and 0<=ny<N: #NxN 안에 있으면
            lst[x][y]=5 #다신 방문할 일 없으니
            x,y = nx,ny #다음으로 이동
        else: break

    #출력
    print(f'#{tc} {ans[0]}', end=' ')
    for i in range(1,len(ans)):
        if ans[i] != ans[i-1]: #연속된 값이면 출력하지 않음
            print(ans[i], end=' ')
    print()

