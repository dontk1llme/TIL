# 1861. 정사각형 방 D4
# BFS라는데요

dx = [-1,1,0,0]
dy = [0,0,1,-1]

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    room = [list(map(int ,input().split())) for _ in range(N)]
    ans = 0
    go = 0 #나중에 하나 더해서 출력해야함. 본인 포함으로 세는 듯

    for i in range(N):
        for j in range(N):
            #아래 두 줄 생각을 못햇네
            tmp_r = 0
            q = [[i,j,0]]
            while q:
                r,c,tmp = q.pop(0)
                tmp_r = max(tmp, tmp_r)
                for k in range(4): #상하좌우 확인
                    nr, nc = r+dx[k] , c+dy[k]
                    if 0<=nr<N and 0<=nc<N:
                        if room[nr][nc]==room[r][c]+1:
                            q.append([nr, nc, tmp+1])
            if go<tmp_r: #최대인 애 출력
                go = tmp_r
                ans = room[i][j]
            elif go==tmp_r: #같은 값이면 룸숫자 작은 애가 답
                if ans > room[i][j]:
                    ans = room[i][j]

    print(f'#{tc} {ans} {go+1}')

#좀 더 내 스타일대로 푼
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

T = int(input())
for t in range(T):
    N = int(input())
    mapp = []
    max_cnt = 0  # 결과값 / 이동한 방의 최대 개수가 저장될 변수
    room = 999999999999  # 결과값 2 / 시작 방번호가 저장될 변수
    for _ in range(N):
        mapp.append(list(map(int, input().split())))
    for x in range(N):  # 모든 x,y 탐색
        for y in range(N):
            cnt = 1
            q = [(x, y)]  # 첫 시작 방 위치 queue에 저장
            while q:  # BFS 탐색 시작 / q가 빌 때까지 q의 요소를 pop 해서 4방향 탐색 조건 만족시 append
                qq = q.pop()
                for i in range(4):
                    if 0 <= qq[0] + dx[i] < N and 0 <= qq[1] + dy[i] < N and (
                            mapp[qq[0] + dx[i]][qq[1] + dy[i]] - mapp[qq[0]][qq[1]] == 1):
                        cnt += 1
                        q.append((qq[0] + dx[i], qq[1] + dy[i]))
            if cnt > max_cnt:  # 탐색 종료 후 건너온 방의 개수가 현재까지 저장된 최대 방 건너온 개수와 비교해서 더 많다면
                max_cnt = cnt  # cnt가 이제 최대 방 건너온 개수가 됨
                room = mapp[x][y]  # room에 위치 저장
            elif cnt == max_cnt:  # 건너온 개수가 같다면
                if mapp[x][y] < room:  # 저장된 방 번호와 비교해 작은지 판단
                    room = mapp[x][y]

    print('#{} {} {}'.format(t + 1, room, max_cnt))
