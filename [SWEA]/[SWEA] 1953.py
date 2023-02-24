# 1953 [모의 SW 역량테스트] 탈주범 검거 (제출용) D4
# BFS틀, 4방향/범위내, 조건-> Q삽입

#파이프
# 0 상 1 하 2 좌 3 우
p = [[],[0,1,2,3],[0,1],[2,3],[0,3],[1,3],[1,2],[0,2]]
opp = {0:1, 1:0, 2:3, 3:2} #필요한 연결되는 방향
di,dj = [-1,1,0,0], [0,0,-1,1] #상하좌우
def bfs(si, sj, L):
    q = [] #[0]
    v = [[0]* M for _ in range(N)] #가로세로 다를 때 주의

    q.append((si, sj))
    v[si][sj]=1
    cnt=1

    while q:
        ci,cj = q.pop(0)
        if v[ci][cj]==L:#종료
            return cnt

        for dr in p[lst[ci][cj]]:  # 현재위치 파이프에 연결된 방향 하나씩 처리
            ni, nj = ci + di[dr], cj + dj[dr]
            if 0 <= ni < N and 0 <= nj < M and v[ni][nj] == 0 and \
                    opp[dr] in p[lst[ni][nj]]:  # 내 방향으로 연결된 파이프가 이동할 방향에 있다면..
                q.append((ni, nj))
                v[ni][nj] = v[ci][cj] + 1
                cnt += 1
    # 공간이 좁아서 L일 전에 모두 방문
    return cnt

T = int(input())
for tc in range(1,T+1):
    N,M,R,C,L = map(int, input().split()) #세로, 가로, 세로위치, 가로위치, 시간
    lst = [list(map(int, input().split())) for _ in range(N)]

    ans = bfs(R,C,L)
    print(f'#{tc} {ans}')
