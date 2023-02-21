def bfs(si, sj, ei, ej):
    # [1] q, v[], 등 생성
    q = []
    v = [[0] * N for _ in range(N)]

    # [2] q에 초기데이터(들) 삽입, v표시
    q.append((si, sj))
    v[si][sj] = 1

    while q:
        ci, cj = q.pop(0)
        # 정답처리는 이곳에서...
        if (ci, cj) == (ei, ej):
            return 1

        # [3] 4방향 반복해서 처리
        for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            ni, nj = ci + di, cj + dj
            # 범위내, 미방문, 조건에 맞으면(벽이 아니면 !='1')
            if 0 <= ni < N and 0 <= nj < N and v[ni][nj] == 0 and arr[ni][nj] != '1':
                q.append((ni, nj))
                v[ni][nj] = v[ci][cj] + 1  # 이동 거리를 저장

    return 0  # 큐가 빌때까지 탐색했지만 리턴 못한 경우 => 막힌 경로


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [input() for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if arr[i][j] == '2':
                si, sj = i, j
            elif arr[i][j] == '3':
                ei, ej = i, j

    ans = bfs(si, sj, ei, ej)
    print(f'#{tc} {ans}')