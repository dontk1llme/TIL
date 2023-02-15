# 고대 유적 (제출용) D2

T = int(input())
for tc in range(1, T+1):
    N,M = map(int,input().split())
    ground = [list(map(int, input().split())) for _ in range(M)]

    #가로
    now = []
    for i in range(N):
        cnt=0
        for j in range(M):
            if ground[i][j] ==1: #1 개수 세다가
                cnt+=1
            else: #1 아니면 개수 더해주고 cnt=0
                if cnt!=0:
                    now.append(cnt)
                    cnt=0
        if cnt!=0: #여기 주의. 마지막 수가 1이면 안 더해줫엇음. 걍 여기선 해줘야해
            now.append(cnt)
    #세로
    for i in range(N):
        cnt=0
        for j in range(M):
            if ground[j][i] ==1:
                cnt+=1
            else:
                if cnt != 0:
                    now.append(cnt)
                    cnt=0
        if cnt!=0:
            now.append(cnt)

    #max
    print(f'#{tc} {max(now)}')

